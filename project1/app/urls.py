from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index_page"),
    path("sample/", views.divisible, name="sample_page"),
    path("sum_of_two/<int:a>/<int:b>", views.sum_of_two, name="sum_of_two"),
    # path("grater_than_10/<str:c>", views.grater_than_10, name="grater_than_10"),
    path("upper_case/<str:c>", views.upper_case, name="upper_case"),
    path("even_or_odd/<int:n>", views.even_or_odd, name="even_or_odd"),
    path("vowels/<str:c>", views.vowles, name="vowels"),
    path("count_digits/<int:n>", views.count_digits, name="count_digits"),
    path("type_of_char/<str:c>", views.type_of_char, name="type_of_char"),
    path("assignment/", views.assignment, name="assignment_page"),
    path("leep_year/<int:year>", views.leep_year, name="leep_year"),
    path("employees/", views.employess, name="employees")
]
