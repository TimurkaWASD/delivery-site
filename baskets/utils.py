from django.db import models

class StatusBasket(models.IntegerChoices):
    ORDER_CREATED = 1, ('Корзина создана')
    EMPTY = 2, ('Пустая')
    LOADING = 3, ('Не звершена')
    FILLED = 4, ('Наполнена')
    CHECK_OUT = 5, ('Оплаченная')

