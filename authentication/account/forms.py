from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User




class RegstrationForm(UserCreationForm):
    # non-model fields (keep them here if templates reference them)
    # phone = forms.CharField(max_length=20, required=False)
    # opt_email = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        
class RequestPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email")
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user is associated with this email address.")
        return email
 