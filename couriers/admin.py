from django.contrib import admin
from .models import *

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'status']
