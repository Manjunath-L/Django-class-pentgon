from django.urls import path
from . import views

app_name = "mobile"

urlpatterns = [
    path("add/", views.add_mobile, name="add_mobile"),
    path("show/", views.all_mobiles, name="all_mobiles"),
]
