from django.urls import path
from catalog.views import index, contact, products


urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('products/', products),
]
