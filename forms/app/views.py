from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

# Create your views here.


def add_student(request):
    # if request.method == "GET":
    #     return render(request, "add_student.html")
    if request.method == "POST":
        name = request.POST["name"]
        rollno = request.POST["rollno"]
        std = request.POST["std"]
        sec = request.POST["sec"]
        gender = request.POST["gender"]
        Student.objects.create(
            rollno=rollno, name=name, std=std, sec=sec, gender=gender
        )
        # return HttpResponse(
        #     f"Student {name} with roll number {rollno} added successfully in class {std} section {sec} with gender {gender} To DataBase."
        # )
        return redirect("app:show_student")
    return render(request, "add_student.html")


def show_student(request):
    qs = Student.objects.all()
    context = {"students": qs}
    return render(request, "show_student.html", context)


def update_student(request, pk):
    stu = Student.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST["name"]
        rollno = request.POST["rollno"]
        std = request.POST["std"]
        sec = request.POST["sec"]
        gender = request.POST["gender"]

        stu.name = name
        stu.rollno = rollno
        stu.std = std
        stu.sec = sec
        stu.gender = gender
        stu.save()
        return redirect("app:show_student")
    context = {"student": stu}
    return render(request, "update_student.html", context)
