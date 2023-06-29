from app.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = {'email', 'name', 'password1', 'password2'}
        ordering = ['password1', 'password2', 'email', 'name']

