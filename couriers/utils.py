from django.db import models

class StatusCourier(models.IntegerChoices):
     AVAILABLE_FOR_ORDER = (1, 'Доступен для назначения заказа')
     WAY_TO_ORDER = (2, 'В пути к получению заказу')
     RECEIVED_AN_ORDER = (3, 'Получил заказ')
     WAY_TO_DELIVERY_POINT = (4, 'В пути к месту доставки')
     COMPLETED_DELIVERY = (5, 'Завершил доставку')
     NOT_ACTIVE = (6, 'Не работает')
     ACTIVE = (7, 'Работает')
