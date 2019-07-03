import logging

from celery import shared_task
from django.db import transaction

from handler.models import Sensor2, Sensor2Rule, Result, ImportState
from handler.tasks.sensor import import_sensor

_l = logging.getLogger(__name__)


@shared_task(name='import_sensor2', ignore_result=True)
def import_sensor2():
    import_sensor('sensor2', Sensor2, Sensor2Rule)


@shared_task(name='reimport_sensor2', ignore_result=True)
def reimport_sensor2():
    with transaction.atomic():
        ImportState.objects.filter(sensor='sensor2').delete()
        Result.objects.filter(sensor='sensor2').delete()
        transaction.on_commit(lambda: import_sensor2.delay())
