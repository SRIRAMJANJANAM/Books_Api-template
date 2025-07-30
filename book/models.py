
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication = models.CharField(max_length=120)
    year = models.DateField()
    class Meta:
        app_label = 'book'
