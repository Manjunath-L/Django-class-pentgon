from . import views
from django.urls import path

urlpatterns = [
    path("", views.user_data, name="user_data"),
]
