from django import forms
from .models import Event, Event_categort


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "event_data": forms.DateInput(attrs={"type": "date"}),
            "event_categort": forms.Select(attrs={"class": "form-select"}),
        }


class Event_categortForm(forms.ModelForm):
    class Meta:
        model = Event_categort
        fields = "__all__"
