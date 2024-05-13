from rest_framework import serializers
from .models import Products, Categories, Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'user', 'name', 'description', 'address', 'rating', 'image', 'is_work', 'city']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', ]

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ['restaurant']
        read_only_fields = ['id']

    def create(self, validated_data):
        # validated_data['restaurant'] = Restaurant.objects.get(pk=self.context.get("restaurant_id"))
        validated_data['restaurant_id'] = self.context.get("restaurant_id")
        return Products.objects.create(**validated_data)

# class RestaurantSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # class Meta:
        # model = Restaurant
        # fields = '__all__'

