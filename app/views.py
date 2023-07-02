from django.shortcuts import render
from category.models import Product

def index(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:10]
    return render(request, 'app/index.html', {
        'products': products
    })

def about(request):
    return render(request, 'app/about.html')