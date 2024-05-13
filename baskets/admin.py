from django.contrib import admin
from .models import *

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total', 'status']

@admin.register(Basket_product)
class BasketProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'basket', 'total', 'quantity']
