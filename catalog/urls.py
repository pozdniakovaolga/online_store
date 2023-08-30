from django.urls import path
from catalog.views import IndexView, ProductListView, ContactView, ProductCreateView
from catalog.views import ProductDetailView, ProductUpdateView, ProductDeleteView, AccessErrorView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('403error/', AccessErrorView.as_view(), name='access_error'),
]
