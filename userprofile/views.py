from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from app.models import User

from .models import UserProfile

def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user
    })


def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

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
