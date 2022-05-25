from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    isbn = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
