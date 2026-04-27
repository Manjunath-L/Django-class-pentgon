from django.contrib import admin

# Register your models here.
from .models import Event, Event_categort

# admin.site.register(Event)
# admin.site.register(Event_categort)


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "event_categort", "event_data", "venue", "image")


admin.site.register(Event, EventAdmin)


class Event_categortAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Event_categort, Event_categortAdmin)
