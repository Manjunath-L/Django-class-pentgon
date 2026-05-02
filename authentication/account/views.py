from re import M

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegstrationForm, RequestPasswordResetForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = RegstrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:home")
        context = {"form": form}
        return render(request, "signup.html", context)
    context = {"form": RegstrationForm()}
    return render(request, "signup.html", context)


# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("account:home")
#         context = {"form": form}
#         return render(request, "signup.html", context)
#     context = {"form": UserCreationForm()}
#     return render(request, "signup.html", context)


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user_obj = form.get_user()
            login(request, user_obj)
            # return HttpResponse(f"Welcome back, {user_obj.username}!")
            return redirect("account:home")
        context = {"form": form}
        return render(request, "signin.html", context)
    context = {"form": AuthenticationForm()}
    return render(request, "signin.html", context)


@login_required(login_url="account:signin")
def home(request):
    return render(request, "home.html")


@login_required(login_url="account:signin")
def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect("account:signin")
    return render(request, "signout.html")


# @login_required(login_url="account:signin")
# def passwordchange(request , pk):
#     user = User.objects.get(id=pk)
#     if request.method == "POST":
#         form = PasswordChangeForm(user=user , data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("account:signin")
#         context = {"form": form}
#         return render(request, "passwordchange.html", context)
#     context = {"form": PasswordChangeForm(user=user)}
#     return render(request, "passwordchange.html", context)


@login_required(login_url="account:signin")
def passwordchange(request, pk):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:signin")
        context = {"form": form}
        return render(request, "passwordchange.html", context)
    context = {"form": PasswordChangeForm(user=request.user)}
    return render(request, "passwordchange.html", context)


def request_reset_password(request):
    if request.method == "POST":
        form = RequestPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            # Here you would typically send a password reset email to the user
            # For demonstration, we'll just redirect to the signin page
            user = User.objects.get(email=email)
            url = f"http://localhost:8000/reset-password/{user.id}/"
            send_mail(
                "reset your password",
                f"Click the link below to reset your password: {url}",
                "radhamanjuradhamanju83@gmail.com",
                [user.email],
            )
            return HttpResponse("Password reset email sent. Please check your inbox.")
        context = {"form": form}
        return render(request, "request_password_reset.html", context)
    context = {"form": RequestPasswordResetForm()}
    return render(request, "request_password_reset.html", context)


def reset_password(request, id):
    user_obj = User.objects.get(id=id)
    if request.method == "POST":
        form = PasswordChangeForm(user=user_obj, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your password has been reset successfully. Please sign in with your new password.",
            )
        context = {"form": form}
        return render(request, "passwordchange.html", context)
    context = {"form": PasswordChangeForm(user=user_obj)}
    return render(request, "passwordchange.html", context)
