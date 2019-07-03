import logging

from celery import shared_task
from django.db import transaction

from handler.models import Sensor1, Sensor1Rule, Result, ImportState
from handler.tasks.sensor import import_sensor

_l = logging.getLogger(__name__)


@shared_task(name='import_sensor1', ignore_result=True)
def import_sensor1():
    import_sensor('sensor1', Sensor1, Sensor1Rule)


@shared_task(name='reimport_sensor1', ignore_result=True)
def reimport_sensor1():
    with transaction.atomic():
        ImportState.objects.filter(sensor='sensor1').delete()
        Result.objects.filter(sensor='sensor1').delete()
        transaction.on_commit(lambda: import_sensor1.delay())
