from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from expenses.models import Category

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create a default admin user if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
            self.stdout.write('Superuser created')