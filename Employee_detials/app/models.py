from django.db import models

# # Create your models here.


class Employee(models.Model):
    deptno = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_join = models.DateField()
    age = models.IntegerField()
    salary = models.IntegerField()
    department = models.CharField(max_length=100)
