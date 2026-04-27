from django.db import models

# Create your models here.
class user_module(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    ph_no = models.IntegerField()
    
    def __str__(self):
        return self.name