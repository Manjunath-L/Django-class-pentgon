from django.shortcuts import render, redirect
from .forms import user_form
from .models import user_module

# Create your views here.


def add_user(request):
    if request.method == "POST":
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("module_forms:all_users")
        context = {"form": form}
        return render(request, "user_data/add_user.html", context)
    context = {"form": user_form()}
    return render(request, "user_data/add_user.html", context)


def all_users(request):
    try:
        users = user_module.objects.all()
        if not users.exists():
            return render(
                request,
                "user_data/all_users.html",
                {"users": users, "error_message": "No users found."},
            )
        return render(request, "user_data/all_users.html", {"users": users})
    except Exception:
        return render(
            request,
            "user_data/all_users.html",
            {
                "users": [],
                "error_message": "Unable to load users right now. Please try again.",
            },
        )


def update_user(request, id):
    user = user_module.objects.get(id=id)
    if request.method == "POST":
        form = user_form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("module_forms:all_users")
        context = {"form": form}
        return render(request, "user_data/edit_user.html", context)
    context = {"form": user_form(instance=user)}
    return render(request, "user_data/edit_user.html", context)


def delete_user(request, id):
    user = user_module.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect("module_forms:all_users")
    context = {"user": user}
    return render(request, "user_data/delete_user.html", context)
