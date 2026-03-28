from . import views
from django.urls import path

urlpatterns = [
    path("", views.product_data, name="product_data"),
]
