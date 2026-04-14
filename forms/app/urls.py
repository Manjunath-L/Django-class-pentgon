from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    # Add your URL patterns here
    path("add_student/", views.add_student, name="add_student"),
    path("show_student/", views.show_student, name="show_student"),
    path("update_student/<int:pk>", views.update_student, name="update_student"),
]
