from django.core.management import BaseCommand
from users.models import User
from config import localconfig


class Command(BaseCommand):
    """Создание superuser"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@pizzaboss.ru',
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password(localconfig.ADMIN_PASSWORD)
        user.save()
