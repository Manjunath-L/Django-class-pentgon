from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm
from .models import Products

# Create your views here.


def add_product(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        qty = request.POST["qty"]
        rating = request.POST["rating"]
        return HttpResponse(
            f"Name: {name}, Price: {price}, Qty: {qty}, Rating: {rating}"
        )
    context = {"form": ProductForm()}
    return render(request, "add_product.html", context)


