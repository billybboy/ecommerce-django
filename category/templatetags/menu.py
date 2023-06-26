"""
customized menu tag
"""

from django import template
from category.models import Category

register = template.Library()

@register.inclusion_tag('app/menu.html')
def menu():
    categories = Category.objects.all()
    return {
        'categories': categories
    }