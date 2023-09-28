from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    country = models.CharField(max_length=50, verbose_name='страна')

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ('last_name',)
