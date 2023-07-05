from django.contrib import admin
from .models import Category, Product, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ['title']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['title']
    search_fields = ['title']

admin.site.register(Order)
admin.site.register(OrderItem)

