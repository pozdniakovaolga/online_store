from django.core.management import BaseCommand
from catalog.models import Category
import json


class Command(BaseCommand):
    """Заполняет данные в базу данных, при этом предварительно зачищает ее от старых данных"""
    def handle(self, *args, **options):
        Category.objects.all().delete()
        with open("data.json", "r", encoding='utf8') as file:
            categories = json.load(file)
            for category in categories:
                name = category['fields']['title']
                descr = category['fields']['description']
                Category.objects.create(
                    title=name,
                    description=descr
                )
