from django.db import models
from baskets.models import Basket
from couriers.models import Courier
from customers.models import Customer
from orders.utils import StatusDelivery, StatusPaymentMethod, StatusOrderRestaurant, PaymentMethod
from restaurants.models import Restaurant


class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name='Корзина')
    order_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время заказа')
    total_amount = models.IntegerField(verbose_name='Общая сумма')
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE, verbose_name='Ресторан')
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    status = models.SmallIntegerField(choices=StatusOrderRestaurant, default=StatusOrderRestaurant.CREATED_ORDER, verbose_name='статус')
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class Review_orders(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ', null=True, blank=True)
    text = models.TextField(verbose_name='Отзыв', blank=True)
    rating = models.IntegerField(verbose_name='Рейтинг', null=True, blank=True)
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Delivery(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ')
    delivery_datetime = models.DateTimeField(verbose_name='Время доставки', null=True, blank=True)
    status = models.SmallIntegerField(choices=StatusDelivery, default=StatusDelivery.ORDER_PROCESSED, verbose_name="Статус")
    start_order_datetime = models.DateTimeField(verbose_name='Время начала доставки', null=True, blank=True)
    end_order_datetime = models.DateTimeField(verbose_name='Время окончания доставки', null=True, blank=True)
    courier = models.ForeignKey(to=Courier, on_delete=models.CASCADE, verbose_name='Курьер', null=True, blank=True)
    
    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"


class Payment_method(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ')
    payment_datetime = models.DateTimeField(verbose_name='Дата оплаты')
    payment_methods = models.IntegerField(choices=PaymentMethod.choices, verbose_name='Метод оплаты')
    status = models.SmallIntegerField(choices=StatusPaymentMethod, default=StatusPaymentMethod.PAYMENT_PENDING, verbose_name="Статус")
    
    class Meta:
        verbose_name = "Метод оплаты"
        verbose_name_plural = "Методы оплат"
