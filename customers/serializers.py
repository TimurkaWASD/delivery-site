from rest_framework import serializers
from customers.models import City, Customer, Customer_address

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'first_name', 'last_name']  # Include any other fields as needed
        read_only_fields = ['id']  # Assuming 'id' is auto-generated and read-only

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_address
        fields = '__all__'



