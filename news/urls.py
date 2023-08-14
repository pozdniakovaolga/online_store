from django.urls import path
from news.views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView
from news.apps import NewsConfig

app_name = NewsConfig.name

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('', ArticleListView.as_view(), name='list'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
]
