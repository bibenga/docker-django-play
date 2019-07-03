from datetime import timedelta
from random import Random

from django.core.management.base import BaseCommand
from django.utils import timezone

from sensor.models import Sensor1


class Command(BaseCommand):
    help = 'Generate test data for sensor1'

    def add_arguments(self, parser):
        parser.add_argument('--clean', action='store_true', help='delete all data', )

        parser.add_argument('--fill', action='store_true', help='generate historical data', )

    def handle(self, *args, **options):
        r = Random()

        if options['clean']:
            Sensor1.objects.all().delete()

        if options['fill']:
            for code in range(1000):
                Sensor1.objects.update_or_create(
                    code=str(code),
                    defaults={
                        'moment': timezone.now() - timedelta(seconds=r.randint(0, 10000)),
                        'value': r.random()
                    }
                )
            return

        changed = 0
        for code in range(1000):
            if r.random() > 0.8:
                Sensor1.objects.update_or_create(
                    code=str(code),
                    defaults={'moment': timezone.now(), 'value': r.random()}
                )
                changed += 1

        self.stdout.write(f'changed = {changed}')

