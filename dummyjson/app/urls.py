from . import views
from django.urls import path

urlpatterns = [
    path("", views.product_data, name="product_data"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),

]
