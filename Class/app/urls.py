from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name= "home"),
    path("add_class/",views.add_class,name="add_class"),
    path("update/<slug:slug>/",views.update_class,name="update_class"),
    path("delete/<slug:slug>/",views.delete_class,name="delete_class")
]

