from calendar import c

from django.http import HttpResponse
from django.shortcuts import render

import re

# Create your views here.
# def index(request):
#     return render(request,'index.html')


def team(request):
    context = {
        "name": "Manjunath L",
        "place": "Bangalore",
        "para": "This is a simple paragraph.",
        "va": ["a", "b", "c", "d"],
        "emp": {
            "name": "Manjunath L",
            "age": 22,
            "sal": 35000,
        },
    }
    return render(request, "index.html", context)


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")  # get input value

        context = {"name": name, "place": "Bangalore"}

        context = {
            "emp": {"name": "john"},
            "sentence": "I love django",
            "word": "madam",
        }
        print(request.POST)  # print all post data
        return render(request, "index.html", context)

    return render(request, "index.html")


def divisible(request):
    context = {"num": 10, "word": "Hello World"}
    return render(request, "sample.html", context)


def sum_of_two(request, a, b):
    context = {"a": a, "b": b, "c": a + b}
    return render(request, "sample.html", context)


def grater_than_10(request, n):
    context = {"n": n}
    return render(request, "if.html", context)


def upper_case(request, c):
    context = {"c": c}
    return render(request, "if.html", context)


def even_or_odd(request, n):
    context = {"n": n}
    return render(request, "ifelse.html", context)


def vowles(request, c):
    context = {"c": c, "vowels": "aeiouAEIOU"}
    return render(request, "vowels.html", context)


def count_digits(request, n):
    context = {"n": n}
    return render(request, "count_number.html", context)


def type_of_char(request, c):
    context = {"c": c}
    return render(request, "type_of_char.html", context)


def assignment(request):
    context = {
        "marks": 65,
        "age": 22,
        "number": 7,
        "c": "a",
        "vowels": ["a", "e", "i", "o", "u"],
        "username": "Manju",
        "temp": 28,
        "salary": 30000,
    }
    return render(request, "assignment.html", context)


def leep_year(request, year):
    context = {"year": year}
    return render(request, "leep_year.html", context)


def employess(request):
    context = {
        "employees": [
            {"name": "Alice", "age": 30, "department": "HR"},
            {"name": "Bob", "age": 25, "department": "IT"},
            {"name": "Charlie", "age": 35, "department": "Finance"},
            {"name": "David", "age": 28, "department": "Marketing"},
            {"name": "Eve", "age": 32, "department": "Sales"},
            {"name": "Frank", "age": 27, "department": "Support"},
            {"name": "Grace", "age": 29, "department": "Development"},
            {"name": "Heidi", "age": 31, "department": "Operations"},
            {"name": "Ivan", "age": 26, "department": "Research"},
            {"name": "Judy", "age": 33, "department": "Administration"},
            {"name": "Karl", "age": 24, "department": "Design"},
            {"name": "Leo", "age": 34, "department": "Logistics"},
        ]
    }
    return render(request, "employees.html", context)
