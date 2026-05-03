from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "doctor_name",
            "specialization",
            "year_of_experience",
            "contact_number",
            "doctor_photo",
        ]
