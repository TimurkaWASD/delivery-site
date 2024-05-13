from rest_framework import serializers

from baskets.models import Basket
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'phone_number', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['id', 'customer', 'total', 'status']