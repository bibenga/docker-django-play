import logging

from django.db import transaction

from handler.models import ImportState, Result
import simpleeval

_l = logging.getLogger(__name__)


# Импортируем только данные с использованием формул
def import_sensor(sensor, sensor_model, sensor_rule_model):
    # Это наше состояние, теоретически на нем можно еще лок сдлеать
    state, _ = ImportState.objects.get_or_create(sensor=sensor)

    # грузим формулы
    rules = {s.code or '': s for s in sensor_rule_model.objects.all()}
    _l.info('loaded rules: %s', rules)

    qs = sensor_model.objects.using('sensor')
    if state.moment:
        qs = qs.filter(moment__gt=state.moment)

    _l.info('%s changes: count=%s', sensor, qs.count())

    if not qs.exists():
        return

    # Нужно для серверного курсора
    with transaction.atomic('sensor'):
        moment = state.moment
        for src in qs.iterator():
            if moment:
                moment = max(moment, src.moment)
            else:
                moment = src.moment

            try:
                # Формула по коду у нас есть?
                rule = rules[src.code]
            except KeyError:
                # Формула по умолчанию у нас есть?
                rule = rules.get('')
            # _l.info('rule: %s', rule)

            value = src.value

            if rule and rule.value_expr:
                try:
                    value = simpleeval.simple_eval(rule.value_expr, names={'value': value})
                except (SyntaxError, TypeError, ValueError):
                    _l.error('Expression error', exc_info=True)
                    # отправить уведомление админу или еще кому нибудь
                    continue

            Result.objects.update_or_create(
                sensor=sensor,
                source_id=src.id,
                defaults={'code': src.code, 'moment': src.moment, 'value': value}
            )

    state.moment = moment
    state.save()
