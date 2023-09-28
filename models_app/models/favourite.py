from django.db import models

from models_app.models.book import Book
from users.models import User


class Favourite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True, verbose_name='книга')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='пользователь')

    class Meta:
        verbose_name = 'избранное'
        verbose_name_plural = 'избранные'
        ordering = ('book',)
