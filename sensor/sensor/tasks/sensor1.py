import logging

from celery import shared_task

from sensor.models import Sensor1
from sensor.tasks.sensor import generate_sensor

_l = logging.getLogger(__name__)


@shared_task(name='generate_sensor1', ignore_result=True)
def generate_sensor1():
    generate_sensor(Sensor1, total=10)
