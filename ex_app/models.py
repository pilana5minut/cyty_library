from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='название книги')
    author = models.CharField(max_length=255, verbose_name='автор книги')
    sbin = models.CharField(max_length=20, verbose_name='SBIN')
    pages = models.IntegerField(verbose_name='кол. страниц')
    status = models.BooleanField(default=True, verbose_name='наличие книги')

    def __str__(self):
        return f'{self.title} - {self.author}'

    class Meta():
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ['title',]
