from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("add_car/", views.add_car, name="add_car"),
    path("show_cars/", views.show_cars, name="show_cars"),
]
