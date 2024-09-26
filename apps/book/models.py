from django.db import models

from apps.book.contant import LANGUAGE

# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=155,
    )
    author = models.CharField(
        max_length=155,
    )
    published_date = models.DateField(
        auto_now_add=True
    )
    isbn = models.CharField(
        max_length=155,
    )
    page_count = models.IntegerField()
    language = models.CharField(
        choices=LANGUAGE,
        max_length=100
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Книги'