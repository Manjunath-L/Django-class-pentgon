from django.shortcuts import redirect, render

# Create your views here.
from .forms import ProductForm
from django.http import HttpResponse
from .models import Product

def add_product(request):
    if request.method =='POST':
        fm=ProductForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse('Product added successfully')
        context={'form':fm}
        return render(request,'add_product.html',context)
    context={'form':ProductForm()}
    return render(request,'add_product.html',context)

def all_products(request):
    qs=Product.objects.all()
    context={'products':qs}
    return render(request,'all_product.html',context)

def update_product(request,pk):
    obj=Product.objects.get(pk=pk)
    if request.method =='POST':
        fm=ProductForm(data=request.POST,instance=obj)
        if fm.is_valid():
            fm.save()
            return redirect('all_products')
        context={'form':fm}
        return render(request,'update_product.html',context)
    context={'form':ProductForm(instance=obj)}
    return render(request,'update_product.html',context)

def delete_product(request,pk):
    obj=Product.objects.get(pk=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('all_products')
    context={'product':obj}
    return render(request,'delete_product.html',context)