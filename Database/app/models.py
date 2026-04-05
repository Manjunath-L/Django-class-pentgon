from django.db import models


# Create your models here.
class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    std = models.IntegerField()
    gender = models.CharField(max_length=10)

