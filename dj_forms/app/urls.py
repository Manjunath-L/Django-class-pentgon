from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("add-product/", views.add_product, name="add_product"),
]
