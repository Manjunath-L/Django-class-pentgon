from django.shortcuts import render

# Create your views here.

# file = open(r'C:\Users\radha\Desktop\dj\users.json', "r")
# json_data = file.read()
# file.close()

# import json

# py_data = json.loads(json_data)


# def user_data(request):
#     context = {"users": py_data["users"]}
#     print(type(json_data), "json_data")
#     print(type(py_data), "python_data")
#     return render(request, "index.html", context)

import json

with open(r"C:\Users\radha\Desktop\dj\products.json", "r", errors="ignore") as file:
    json_data = file.read()

py_data = json.loads(json_data)


def product_data(request):
    context = {"products": py_data["products"]}
    print(type(json_data), "json_data")
    print(type(py_data), "python_data")
    return render(request, "index.html", context)
