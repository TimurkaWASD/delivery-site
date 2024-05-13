from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from couriers.permissions import IsCourier
from orders.models import Delivery
from orders.serializers import DeliverySerializer

class CourierOrdersListView(ListAPIView): # Просмотр заказов курьером, которые связаны с ним
    serializer_class = DeliverySerializer
    permission_classes = [IsCourier]

    def get_queryset(self):
        # Возвращаем только заказы, связанные с текущим курьером
        return Delivery.objects.all()

class CourierDeliveryAcceptView(APIView): # принятие заказов курьером
    serializer_class = DeliverySerializer
    permission_classes = [IsCourier]

    def post(self, request):
        delivery = Delivery.objects.get(pk=request.data.get('delivery_id'))
        delivery.courier = request.user.courier
        delivery.save()
        return Response({'order': delivery.id,}, status=status.HTTP_200_OK)
