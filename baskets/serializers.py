from rest_framework import serializers
from baskets.models import Basket, Basket_product
from restaurants.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class BasketProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket_product
        fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'