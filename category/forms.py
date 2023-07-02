from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'price', 'description', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'p-2 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'p-2 border border-gray-200'
            }),
            'price': forms.TextInput(attrs={
                'class': 'p-2 border border-gray-200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'p-2 border border-gray-200'
            }),
        }