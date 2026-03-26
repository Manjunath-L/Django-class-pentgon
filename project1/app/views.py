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
