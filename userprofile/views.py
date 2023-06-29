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

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user
    })

@login_required
def mystore(request):
    return render(request, 'userprofile/mystore.html')

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

            return redirect('userprofile:mystore')

    else:
        form = ProductForm()

    return render(request, 'userprofile/add_product.html', {
        'title': 'Add Product',
        'form': form
    })

@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    form = ProductForm(instance=product)

    return render(request, 'userprofile/add_product.html', {
        'title': 'Edit Product',
        'form': form
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = UserProfile.objects.create(user=user)

            return redirect('app:index')
    else:
        form = SignUpForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })
