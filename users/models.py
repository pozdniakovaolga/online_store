from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Пользователь"""

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    phone = models.CharField(max_length=30, verbose_name='телефон', blank=True, null=True)
    country = models.CharField(max_length=30, verbose_name='страна', blank=True, null=True)

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
