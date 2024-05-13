from customers.models import *
from baskets.utils import StatusBasket
from restaurants.models import *


class Basket(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    total = models.IntegerField(verbose_name='Сумма')
    status = models.SmallIntegerField(choices=StatusBasket, default=StatusBasket.ORDER_CREATED, verbose_name='Корзина')

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class Basket_product(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Блюдо')
    basket = models.ForeignKey(to=Basket, on_delete=models.CASCADE, verbose_name='Корзина')
    total = models.IntegerField(verbose_name='Сумма')
    quantity = models.IntegerField(verbose_name='Количество')
    class Meta:
        verbose_name = "Продукт из корзины"
        verbose_name_plural = "Продукты из корзины"