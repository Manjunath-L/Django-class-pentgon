from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path("add_event_category/", views.add_event_category, name="add_event_category"),
    path("add_event/", views.add_event, name="add_event"),
    path("view_event_category/", views.view_event_category, name="view_event_category"),
    path("view_event/", views.view_event, name="view_event"),
    # path("update_event/<int:id>/", views.update_event, name="update_event"),
    # path("delete_event/<int:id>/", views.delete_event, name="delete_event"),
]
