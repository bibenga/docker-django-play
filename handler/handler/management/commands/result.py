from django.core.management.base import BaseCommand

from handler.models import Result, ImportState
from handler.tasks.sensor1 import import_sensor1
from handler.tasks.sensor2 import import_sensor2


class Command(BaseCommand):
    help = 'Create admin user for dev mode'

    def add_arguments(self, parser):
        parser.add_argument('--clean', action='store_true', help='delete all data', )

    def handle(self, *args, **options):
        if options['clean']:
            ImportState.objects.all().delete()
            Result.objects.all().delete()

        import_sensor1()
        import_sensor2()
