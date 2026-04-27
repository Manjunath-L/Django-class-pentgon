from django import forms
from .models import user_module


class user_form(forms.ModelForm):
    class Meta:
        model = user_module
        fields = "__all__"
