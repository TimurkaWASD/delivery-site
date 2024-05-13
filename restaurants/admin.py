from django.contrib import admin
from .models import *

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'address', 'rating', 'is_work', 'city']
    

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'rating', 'price', 'size', 'category', 'restaurant', 'is_sale', 'discount']

