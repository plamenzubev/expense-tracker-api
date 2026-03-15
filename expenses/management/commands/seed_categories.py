from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from expenses.models import Category

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from expenses.models import Category

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
            self.stdout.write('Superuser created')

        # Create global categories
        categories = ['Food & Drinks', 'Transport', 'Shopping', 'Entertainment', 'Bills']
        for name in categories:
            Category.objects.get_or_create(name=name, user=None)
            self.stdout.write(f'Category {name} created')
        
        # Make all existing categories global
        Category.objects.all().update(user=None)
        self.stdout.write('All categories set to global')