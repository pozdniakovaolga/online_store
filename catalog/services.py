from catalog.models import Category
from django.conf import settings
from django.core.cache import cache


def get_cashed_category_list():
    """Функция возвращает закешированный список категорий"""

    key = 'categories'
    category_list = Category.objects.all()

    if settings.CACHE_ENABLED:
        categories = cache.get(key)
        if categories is None:
            categories = category_list
            cache.set(key, categories)
        return categories

    return category_list
