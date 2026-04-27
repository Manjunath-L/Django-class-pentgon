from django.shortcuts import render, redirect
from .models import Event, Event_categort
from .forms import EventForm, Event_categortForm
from django.http import HttpResponse


# urlpatterns = [
#     path("add_event_category/", views.add_event_category, name="add_event_category"),
#     path("add_event/", views.add_event, name="add_event"),
#     path("view_event_category/", views.view_event_category, name="view_event_category"),
#     path("view_event/", views.view_event, name="view_event"),
#     path("update_event/<int:id>/", views.update_event, name="update_event"),
#     path("delete_event/<int:id>/", views.delete_event, name="delete_event"),
# ]
# Create your views here.
def add_event_category(request):
    form = Event_categortForm()
    if request.method == "POST":
        form = Event_categortForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event:view_event_category")
        context = {"form": form}
        return render(request, "event/add_event_categort.html", context)
    context = {"form": Event_categortForm()}
    return render(request, "event/add_event_categort.html", context)


def add_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("event:view_event")
        context = {"form": form}
        return render(request, "event/add_event.html", context)
    context = {"form": EventForm()}
    return render(request, "event/add_event.html", context)


def view_event_category(request):
    event_category = Event_categort.objects.all()
    context = {"event_category": event_category}
    return render(request, "event/view_event_category.html", context)


def view_event(request):
    event = Event.objects.all()
    context = {"event": event}
    return render(request, "event/show_event.html", context)

def update_event(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect("event:view_event")
        context = {"form": form}
        return render(request, "event/update_event.html", context)
    context = {"form": form}
    return render(request, "event/update_event.html", context)

def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect("event:view_event")