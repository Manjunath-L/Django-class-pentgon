from pydoc import doc

from django.shortcuts import render, redirect
from .forms import DoctorForm
from django.http import HttpResponse
from .models import Doctor

# Create your views here.


def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance=Doctor())
        if form.is_valid():
            form.save()
            return redirect("all_doctor")
        context = {"form": form}
        return render(request, "add_doctor.html", context)
    context = {"form": DoctorForm()}
    return render(request, "add_doctor.html", context)


def all_doctor(request):
    doctors = Doctor.objects.all()
    context = {"doctors": doctors}
    return render(request, "all_doctors.html", context)


def update_doctor(request, pk, slug):
    doctor = Doctor.objects.get(id=pk, slug=slug)
    form = DoctorForm(instance=doctor)
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("all_doctor")
        context = {"form": form}
        return render(request, "update_doctor.html", context)
    context = {"form": DoctorForm(instance=doctor) }
    return render(request, "update_doctor.html", context)


def delete_doctor(request, pk, slug):
    doctor = Doctor.objects.get(id=pk, slug=slug)
    if request.method == "POST":
        doctor.delete()
        return redirect("all_doctor")
    context = {"doctor": doctor}
    return render(request, "delete_doctor.html", context)
