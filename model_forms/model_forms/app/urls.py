from django.urls import path
from . import views

urlpatterns = [
  path('product/add/', views.add_product, name='add_product'),
  path('products/', views.all_products, name='all_products'),
  path('product/update/<int:pk>/', views.update_product, name='update_product'),
  path('product/delete/<int:pk>/', views.delete_product, name='delete_product'),
]