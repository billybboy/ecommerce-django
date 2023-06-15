from django.shortcuts import render
from category.models import Product

def index(request):
    products = Product.objects.all()[0:10]
    return render(request, 'app/index.html', {
        'products': products
    })

def about(request):
    return render(request, 'app/about.html')