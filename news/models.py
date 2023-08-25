from django.db import models
from django.urls import reverse


class Article(models.Model):
    """Статья"""
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=20, verbose_name='slug', null=True, blank=True,)
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='articles/', null=True, blank=True, verbose_name='Изображение')
    date = models.DateField(verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("news:view", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
