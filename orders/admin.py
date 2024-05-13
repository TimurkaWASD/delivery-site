from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_datetime', 'total_amount', 'restaurant', 'customer']

@admin.register(Review_orders)
class ReviewOrdersAdmin(admin.ModelAdmin):
    list_display = ['order', 'text', 'rating']

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['order', 'delivery_datetime', 'status', 'start_order_datetime', 'end_order_datetime', 'courier']

@admin.register(Payment_method)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment_datetime', 'payment_methods', 'status']