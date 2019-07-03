from datetime import timedelta
from random import Random

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from sensor.models import Sensor2


class Command(BaseCommand):
    help = 'Generate test data for sensor2'

    fake_period = 30 * 24 * 60 * 60

    def add_arguments(self, parser):
        parser.add_argument('--clean', action='store_true', help='delete all data', )

        parser.add_argument('--fill', action='store_true', help='generate data')

    def handle(self, *args, **options):
        r = Random()

        if options['clean']:
            Sensor2.objects.all().delete()

        if options['fill']:
            for code in range(1000):
                Sensor2.objects.update_or_create(
                    code=str(code),
                    defaults={
                        'moment': timezone.now() - timedelta(seconds=r.randint(0, 10000)),
                        'value': r.random()
                    }
                )
            return

        for code in range(1000):
            if r.random() > 0.5:
                Sensor2.objects.update_or_create(
                    code=str(code),
                    defaults={'moment': timezone.now(), 'value': r.random()}
                )

