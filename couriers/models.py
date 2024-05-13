from django.db import models
from couriers.utils import StatusCourier
from user.models import CustomUser

class Courier(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    first_name = models.CharField(max_length=25, verbose_name="Имя")
    status = models.SmallIntegerField(choices=StatusCourier, default=StatusCourier.AVAILABLE_FOR_ORDER, verbose_name="Статус")
    photo = models.ImageField(upload_to='images/courier', verbose_name="Аватар", null=True, blank=True, default=None)
    
    class Meta:
        verbose_name = "Курьер"
        verbose_name_plural = "Курьеры"

    def __str__(self):
        return self.first_name