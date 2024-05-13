from django.db import models
from user.models import CustomUser

class Customer(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Card(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    cvv_code = models.CharField(max_length=3, default=None, verbose_name='CVV-код')
    first_name_card = models.CharField(max_length=25, default=None, verbose_name='Имя')
    last_name_card = models.CharField(max_length=25, default=None, verbose_name='Фамилия')
    number_card = models.IntegerField(max_length=16, default=None, verbose_name='Номер Карты')
    
    class Meta:
        verbose_name = "Банковская карта"
        verbose_name_plural = "Банковские карты"

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Город')

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
            
    def __str__(self):
        return self.name

class Customer_address(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    street_address = models.CharField(max_length=75, verbose_name='Адрес')
    house_number = models.IntegerField(blank=True, null=True, verbose_name='Номер квартиры')
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, verbose_name='Город')
    
    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

