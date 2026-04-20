from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.IntegerField()
    qty = forms.IntegerField()
    rating = forms.DecimalField(max_digits=3, decimal_places=2)
    
