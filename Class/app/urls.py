from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name= "home"),
    path("add_class/",views.add_class,name="add_class"),
    path("update/<int:id>/",views.update_class,name="update_class"),
    path("delete/<int:id>/",views.delete_class,name="delete_class")
]

