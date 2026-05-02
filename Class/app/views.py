from django.shortcuts import render, redirect
from .models import Class
from .forms import ClassForm
from django.contrib import messages

# Create your views here.


def home(request):
    classes = Class.objects.all()
    context = {"classes": classes}
    return render(request, "home.html", context)


def add_class(request):
    form = ClassForm()
    if request.method == "POST":
        fm = ClassForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Class added successfully!")
            return redirect("home")
        context = {"form": fm}
        return render(request, "add_class.html", context)
    context = {"form": form}
    return render(request, "add_class.html", context)


def update_class(request, id):
    class_obj = Class.objects.get(id=id)
    form = ClassForm(instance=class_obj)
    if request.method == "POST":
        fm = ClassForm(request.POST, instance=class_obj)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Class updated successfully!")
            return redirect("home")
        context = {"form": fm}
        return render(request, "update_class.html", context)
    context = {"form": form}
    return render(request, "update_class.html", context)


def delete_class(request, id):
    class_obj = Class.objects.get(id=id)
    if request.method == "POST":
        class_obj.delete()
        messages.error(request, "Class deleted successfully!")
        return redirect("home")
    context = {"class_obj": class_obj}
    return render(request, "delete.html", context)
        
