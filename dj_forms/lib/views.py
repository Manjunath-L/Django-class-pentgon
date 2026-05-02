from django.shortcuts import render, redirect
from .forms import BookForm
from .models import BookTables
from django.contrib import messages

# Create your views here.


def add_book(request):
    if request.method == "POST":
        fm = BookForm(request.POST)
        if fm.is_valid():
            title = fm.cleaned_data["title"]
            author = fm.cleaned_data["author"]
            publisher = fm.cleaned_data["publisher"]
            publication_date = fm.cleaned_data["publication_date"]
            price = fm.cleaned_data["price"]
            BookTables.objects.create(
                title=title,
                author=author,
                publisher=publisher,
                publication_date=publication_date,
                price=price,
            )
            messages.add_message(
                request, messages.SUCCESS, f"Book '{title}' added successfully."
            )
            return redirect("lib:show_books")
        context = {"form": fm}
        return render(request, "add_book.html", context)
    context = {"form": BookForm()}
    return render(request, "add_book.html", context)


def show_books(request):
    books = BookTables.objects.all()
    return render(request, "show_books.html", {"books": books})


# def update_book(request, id):
#     book = BookTables.objects.get(id=id)
#     if request.method == "POST":
#         fm = BookForm(request.POST)
#         if fm.is_valid():
#             book.title = fm.cleaned_data["title"]
#             book.author = fm.cleaned_data["author"]
#             book.publisher = fm.cleaned_data["publisher"]
#             book.publication_date = fm.cleaned_data["publication_date"]
#             book.price = fm.cleaned_data["price"]
#             book.save()
#             message.add_message(
#                 request, messages.SUCCESS, f"Book '{book.title}' updated successfully."
#             )
#             return redirect("lib:show_books")
#         context = {"form": fm}
#         return render(request, "update_book.html", context)
#     initial_data = {
#         "title": book.title,
#         "author": book.author,
#         "publisher": book.publisher,
#         "publication_date": book.publication_date,
#         "price": book.price,
#     }
#     context = {"form": BookForm(initial=initial_data)}
#     return render(request, "update_book.html", context)


def update_book(request, id):
    qs = BookTables.objects.filter(id=id)
    obj = qs[0]
    out = qs.values()
    book_data = out[0]
    if request.method == "POST":
        fm = BookForm(data=request.POST)
        if fm.is_valid():
            title = fm.cleaned_data["title"]
            author = fm.cleaned_data["author"]
            publisher = fm.cleaned_data["publisher"]
            publication_date = fm.cleaned_data["publication_date"]
            price = fm.cleaned_data["price"]

            obj.title = title
            obj.author = author
            obj.publisher = publisher
            obj.publication_date = publication_date
            obj.price = price
            obj.save()
            messages.add_message(
                request, messages.SUCCESS, f"Book '{obj.title}' updated successfully."
            )
            return redirect("lib:show_books")

    context = {"form": BookForm(data=book_data)}
    return render(request, "update_book.html", context)


def delete_book(request, id):
    book = BookTables.objects.get(id=id)
    if request.method == "POST":
        book.delete()
        messages.add_message(
            request, messages.ERROR, f"Book '{book.title}' deleted successfully."
        )
        return redirect("lib:show_books")
    return render(request, "delete_book.html", {"book": book})
