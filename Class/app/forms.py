from .models import Class
from django import forms


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ["name", "teacher", "no_students", "batch", "starts_at", "ends_at"]
        widgets = {
            "starts_at": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "ends_at": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
        }
