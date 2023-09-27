from django.db import models

from config import settings


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
        ordering = ('title',)


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    country = models.CharField(max_length=50, verbose_name='страна')

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ('last_name',)


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    author = models.ManyToManyField(Author, on_delete=models.CASCADE, null=True, blank=True, verbose_name='автор')
    description = models.TextField(verbose_name='описание')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True, verbose_name='жанр')
    price = models.IntegerField(default=0, verbose_name='цена')
    pub_year = models.DateTimeField(verbose_name='год издания')

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ('title',)


class Favourite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True, verbose_name='книга')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='пользователь')

    class Meta:
        verbose_name = 'избранное'
        verbose_name_plural = 'избранные'
        ordering = ('book',)
