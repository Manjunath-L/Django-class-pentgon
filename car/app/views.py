from django.shortcuts import render, redirect

from .models import Car


# Create your views here.


def add_car(request):
    if request.method == "POST":
        car_name = request.POST["car_name"]
        car_model = request.POST["car_model"]
        car_color = request.POST["car_color"]
        car_price = request.POST["car_price"]
        Car.objects.create(
            name=car_name, model=car_model, color=car_color, price=car_price
        )
        return redirect("app:show_cars")
    return render(request, "add_car.html")


def show_cars(request):
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, "show_car.html", context)


def update_car(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == "POST":
        car.name = request.POST["car_name"]
        car.model = request.POST["car_model"]
        car.color = request.POST["car_color"]
        car.price = request.POST["car_price"]
        car.save()
        return redirect("app:show_cars")
    context = {"car": car}
    return render(request, "update_car.html", context)
