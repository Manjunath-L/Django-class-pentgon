from django.db import models

# Create your models here.


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    sepcialization = models.CharField(max_length=200)
    year_of_experience = models.IntegerField()
    contect_number = models.IntegerField()
    doctor_photo = models.ImageField(
        upload_to="doctor_profiles/", blank=True, null=True
    )

    def __str__(self):
        return self.doctor_name
