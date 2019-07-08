from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create admin user for dev mode'

    def handle(self, *args, **options):
        if not User.objects.filter(username='a').exists():
            User.objects.create_superuser(username='a', email='a@a.aa', password='a')

        if not User.objects.filter(username='b').exists():
            User.objects.create_superuser(username='b', email='b@b.bb', password='b')
