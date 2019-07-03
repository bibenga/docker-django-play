import logging
from random import Random

from django.utils import timezone

_l = logging.getLogger(__name__)


def generate_sensor(sensor_model, total=1):
    r = Random()
    for code in range(total):
        code = r.randint(0, 1000 - 1)
        sensor_model.objects.update_or_create(
            code=str(code),
            defaults={'moment': timezone.now(), 'value': r.random()}
        )
