from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    #created = models.CharField(max_length=250, default='п/п продукты', verbose_name='Состав')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date = models.DateField(verbose_name='Дата создания')
    last_update = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contacts(models.Model):
    phone_delivery = models.CharField(max_length=50, verbose_name='Телефон доставки')
    phone_seo = models.CharField(max_length=50, verbose_name='Телефон руководства')
    email = models.CharField(max_length=50, verbose_name='E-mail')

    def __str__(self):
        return f'{self.phone_delivery}, {self.phone_seo}, {self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
