from django.http import Http404
from django.shortcuts import render
import json


with open(r"C:\Users\radha\Desktop\dj\recipes.json", "r", errors="ignore") as file:
    json_data = file.read()

py_data = json.loads(json_data)


def recipe_list(request):
    recipes = py_data.get("recipes", [])
    context = {"recipes": recipes}
    return render(request, "index.html", context)


def recipe_detail(request, recipe_id: int):
    recipes = py_data.get("recipes", [])
    recipe = next((r for r in recipes if r.get("id") == recipe_id), None)
    if recipe is None:
        raise Http404("Recipe not found")
    context = {"recipe": recipe}
    return render(request, "recipe_detail.html", context)


def demo(request):
    return render(request, "demo.html")
