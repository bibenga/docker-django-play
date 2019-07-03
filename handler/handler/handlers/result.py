from django.db import transaction
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from handler.models import Sensor1Rule, Sensor2Rule
from handler.tasks import reimport_sensor1, reimport_sensor2

# Удалим все резалты после изменения формулы


@receiver(post_save, sender=Sensor1Rule, dispatch_uid='sensor1rule_post_save')
def sensor1rule_post_save(sender, **kwargs):
    transaction.on_commit(lambda: reimport_sensor1.delay())


@receiver(pre_delete, sender=Sensor1Rule, dispatch_uid='sensor1rule_pre_delete')
def sensor1rule_pre_delete(sender, **kwargs):
    transaction.on_commit(lambda: reimport_sensor1.delay())


@receiver(post_save, sender=Sensor2Rule, dispatch_uid='sensor2rule_post_save')
def sensor2rule_post_save(sender, **kwargs):
    transaction.on_commit(lambda: reimport_sensor2.delay())


@receiver(pre_delete, sender=Sensor2Rule, dispatch_uid='sensor2rule_pre_delete')
def sensor2rule_pre_delete(sender, **kwargs):
    transaction.on_commit(lambda: reimport_sensor2.delay())
