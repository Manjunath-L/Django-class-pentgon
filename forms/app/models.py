from django.db import models

# Create your models here.


class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=100)
    std = models.IntegerField()
    sec = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
