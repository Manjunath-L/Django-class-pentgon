from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    publisher = forms.CharField(max_length=100)
    publication_date = forms.DateField()
    price = forms.IntegerField()
