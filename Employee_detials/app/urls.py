from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("add_emp/", views.add_emp, name="add_emp"),
    path("show_emp/", views.show_emp, name="show_emp"),
    path("update_emp/<int:pk>/", views.update_emp, name="update_emp"),
    path("delete_emp/<int:pk>/", views.delete_emp, name="delete_emp"),
]
