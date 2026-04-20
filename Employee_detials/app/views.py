from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def add_emp(request):
    if request.method == "GET":
        return render(request, "add_emp.html")
    elif request.method == "POST":
        deptno = request.POST.get("deptno")
        name = request.POST.get("name")
        email = request.POST.get("email")
        date_of_join = request.POST.get("date_of_join")
        age = request.POST.get("age")
        salary = request.POST.get("salary")
        department = request.POST.get("department")
        Employee.objects.create(
            deptno=deptno,
            name=name,
            email=email,
            date_of_join=date_of_join,
            age=age,
            salary=salary,
            department=department,
        )
        messages.add_message(
            request, messages.SUCCESS, f"Employee {name} added successfully."
        )
        return redirect("app:show_emp")


def show_emp(request):
    employess = Employee.objects.all()
    return render(request, "show_emp.html", {"employees": employess})


def update_emp(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == "POST":
        deptno = request.POST.get("deptno")
        name = request.POST.get("name")
        email = request.POST.get("email")
        date_of_join = request.POST.get("date_of_join")
        age = request.POST.get("age")
        salary = request.POST.get("salary")
        department = request.POST.get("department")
        emp.deptno = deptno
        emp.name = name
        emp.email = email
        emp.date_of_join = date_of_join
        emp.age = age
        emp.salary = salary
        emp.department = department
        emp.save()
        messages.add_message(
            request, messages.SUCCESS, f"Employee {name} updated successfully."
        )
        return redirect("app:show_emp")
    context = {"employee": emp}
    return render(request, "update_emp.html", context)


def delete_emp(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == "POST":
        emp.delete()
        messages.add_message(
            request, messages.ERROR, f"Employee {emp.name} deleted successfully."
        )
        return redirect("app:show_emp")
    context = {"employee": emp}
    return render(request, "delete_emp.html", context)
