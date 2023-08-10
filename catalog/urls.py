from django.urls import path
from catalog.views import index, contact, products, add_products


urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('products/', products),
    path('add_products/', add_products),
]
