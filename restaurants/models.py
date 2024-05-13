from django.db import models

from customers.models import City
from user.models import CustomUser


class Restaurant(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    address = models.TextField(verbose_name="Адрес")
    rating = models.IntegerField(verbose_name="Рейтинг")
    image = models.ImageField(upload_to='images/restaurants',verbose_name="Фото", null=True, blank=True)
    is_work = models.BooleanField(default=False, verbose_name="Работает")
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, verbose_name="Город")
    
    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"
        
    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    image = models.ImageField(upload_to='images/categories/', verbose_name="Фото")
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    rating = models.IntegerField(verbose_name="Рейтинг")
    price = models.IntegerField(verbose_name="Цена")
    size = models.IntegerField(verbose_name="Размер")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Категория")
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE, verbose_name="Ресторан")
    image = models.ImageField(upload_to='images/products/', verbose_name="Фото")
    is_sale = models.BooleanField(default=False, verbose_name="Акция")
    discount = models.IntegerField(verbose_name="Скидка %")
    
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
    
    def __str__(self):
        return self.name
