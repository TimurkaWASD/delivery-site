from rest_framework import serializers
from couriers.models import Courier


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['id', 'user', 'first_name', 'status', 'photo']  # Include any other fields as needed
        read_only_fields = ['id']  # Assuming 'id' is auto-generated and read-only

    def create(self, validated_data):
        return Courier.objects.create(**validated_data)

