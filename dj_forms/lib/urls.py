from django.urls import path
from . import views

app_name = "lib"

urlpatterns = [
    path("add_book/", views.add_book, name="add_book"),
    path("show_books/", views.show_books, name="show_books"),
    path("update_book/<int:id>/", views.update_book, name="update_book"),
    path("delete_book/<int:id>/", views.delete_book, name="delete_book"),
]
