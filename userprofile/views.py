from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .forms import SignUpForm

from app.models import User
from .models import UserProfile

from category.forms import ProductForm
from category.models import Product


def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user,
        'products': products
    })

@login_required
def mystore(request):
    products = request.user.products.filter(status=Product.ACTIVE)
    return render(request, 'userprofile/mystore.html', {
        'products': products
    })

@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            slug = slugify(title)

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slug
            product.save()

            messages.success(request, 'Product created successfully.')

            return redirect('userprofile:mystore')

    else:
        form = ProductForm()

    return render(request, 'userprofile/product_form.html', {
        'title': 'Add Product',
        'form': form
    })

@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            messages.success(request, 'Product updated.')

            return redirect('userprofile:mystore')



    else:
        form = ProductForm(instance=product)

    return render(request, 'userprofile/product_form.html', {
        'title': 'Edit Product',
        'form': form,
        'product': product
    })

@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, 'Product deleted.')

    return redirect('userprofile:mystore')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = UserProfile.objects.create(user=user)

            messages.success(request, 'You have signup and logged in successfully.')

            return redirect('app:index')
    else:
        form = SignUpForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })
