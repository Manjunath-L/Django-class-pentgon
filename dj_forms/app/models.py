from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
