from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    author = models.ManyToManyField('Author', null=True, blank=True, verbose_name='автор')
    description = models.TextField(verbose_name='описание')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null=True, blank=True, verbose_name='жанр')
    price = models.IntegerField(default=0, verbose_name='цена')
    pub_year = models.DateTimeField(verbose_name='год издания')

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ('title',)
