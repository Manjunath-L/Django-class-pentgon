from email.mime import image

from django.db import models

# Create your models here.


class Event_categort(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    event_categort = models.ForeignKey(Event_categort, on_delete=models.CASCADE)
    event_data = models.DateField()
    venue = models.CharField(max_length=255)
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
