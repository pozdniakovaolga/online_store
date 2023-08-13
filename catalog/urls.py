from django.urls import path
from catalog.views import IndexView, ProductListView, ContactView, ProductCreateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='products'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('add_products/', ProductCreateView.as_view(), name='add_products'),
]
