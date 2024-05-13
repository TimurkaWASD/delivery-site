from django.contrib import admin
from .models import *
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['customer', 'number_card']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Customer_address)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'street_address', 'house_number', 'city']
