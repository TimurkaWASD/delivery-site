from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UpdateOrderStatusSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    new_status = serializers.ChoiceField(choices=StatusOrderRestaurant.choices)

    def validate(self, data):
        order_id = data.get('order_id')
        new_status = data.get('new_status')

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise serializers.ValidationError("Order not found.")

        if order.status == new_status:
            raise serializers.ValidationError("Order status is already set to this value.")

        return data

class UpdateDeliveryStatusSerializer(serializers.Serializer):
    delivery_id = serializers.IntegerField()
    new_status = serializers.ChoiceField(choices=StatusDelivery.choices)

    def validate(self, data):
        delivery_id = data.get('delivery_id')
        new_status = data.get('new_status')

        try:
            delivery = Delivery.objects.get(id=delivery_id)
        except Delivery.DoesNotExist:
            raise serializers.ValidationError("Delivery not found.")

        if delivery.status == new_status:
            raise serializers.ValidationError("Delivery status is already set to this value.")

        return data



class PaymentMethodSerializer(serializers.Serializer):
    class Meta:
        model = Payment_method
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'  # Include any other fields as needed
        read_only_fields = ['id']  # Assuming 'id' is auto-generated and read-only

    def create(self, validated_data):
        return Delivery.objects.create(**validated_data)

class ReviewOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review_orders
        fields = '__all__'

    def create(self, validated_data):
        return Review_orders.objects.create(**validated_data)