from django.urls import path
from . import views

app_name = "module_forms"

urlpatterns = [
    path("add_user/", views.add_user, name="add_user"),
    path("all_users/", views.all_users, name="all_users"),
    path("update_user/<int:id>/", views.update_user, name="update_user"),
    path("delete_user/<int:id>/", views.delete_user, name="delete_user"),
]
