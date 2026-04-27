from django.urls import path
from . import views

urlpatterns = [
    path("add_doctor/", views.add_doctor, name="add_doctor"),
    path("all_doctor/", views.all_doctor, name="all_doctor"),
    path("update_doctor/<int:pk>/", views.update_doctor, name="update_doctor"),
    path("delete_doctor/<int:pk>/", views.delete_doctor, name="delete_doctor"),
]
