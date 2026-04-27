from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MobileForm
from .models import Mobile


# Create your views here.


def add_mobile(request):
    if request.method == "POST":
        fm = MobileForm(request.POST)
        if fm.is_valid():
            brand = fm.cleaned_data["brand"]
            model = fm.cleaned_data["model"]
            price = fm.cleaned_data["price"]
            rom = fm.cleaned_data["rom"]
            ram = fm.cleaned_data["ram"]
            battery = fm.cleaned_data["battery"]
            Mobile.objects.create(
                brand=brand, model=model, price=price, rom=rom, ram=ram, battery=battery
            )
            return redirect("mobile:all_mobiles")
        context = {"form": fm}
        return render(request, "mobile/add_mobile.html", context)
    context = {"form": MobileForm()}
    return render(request, "mobile/add_mobile.html", context)


# def update_mobile(request,id):
#     if request.method == "POST"

def all_mobiles(request):
    mobiles = Mobile.objects.all()
    context = {"mobiles": mobiles}
    return render(request, "mobile/all_mobiles.html", context)
