import logging

from celery import shared_task

from sensor.models import Sensor2
from sensor.tasks.sensor import generate_sensor

_l = logging.getLogger(__name__)


@shared_task(name='generate_sensor2', ignore_result=True)
def generate_sensor2():
    generate_sensor(Sensor2, total=50)
