from django.db import models

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    no_students = models.IntegerField()
    batch = models.CharField(max_length=10)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()

    def __str__(self):
        return self.name
