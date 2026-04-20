from django.db import models

# Create your models here.

class BookTables(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.IntegerField()
