from django.http import HttpResponse
from .models import Customer, City, Customer_address, Card
from .serializers import CustomerSerializer,CitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from user.permissions import IsCustomer



def index(request):
    return HttpResponse("ku")


class AddCustomerAddressAPIView(APIView): # добавление адреса курьера
    permission_classes = [IsCustomer]

    def post(self, request):

        user = request.user
        customer = user.customer

        street_address = request.data.get('street_address')
        house_number = request.data.get('house_number')
        city_id = request.data.get('city')

        try:
            city = City.objects.get(id=city_id)
        except City.DoesNotExist:
            return Response({'error': 'Город не найден'}, status=status.HTTP_404_NOT_FOUND)

        customer_address =  Customer_address.objects.create(
            city=city,
            customer=customer,
            street_address=street_address,
            house_number=house_number,
        )

        return Response({'success': 'Адрес успешно добавлен'}, status=status.HTTP_201_CREATED)

class AddCustomerCardAPIView(APIView): # добавление кредитной карты пользователя
    permission_classes = [IsCustomer]

    def post(self, request):
        user = request.user
        customer = user.customer

        cvv_code =  request.data.get('cvv_code')
        number_card = request.data.get('number_card')
        first_name_card = request.data.get('first_name')
        last_name_card = request.data.get('last_name')

        card = Card.objects.create(
            number_card=number_card,
            cvv_code=cvv_code,
            first_name_card=first_name_card,
            last_name_card=last_name_card,
            customer=customer,
        )

        return Response({'success': 'Карта добавлена'}, status=status.HTTP_201_CREATED)


"""-------------------------------------------------- api -----------------------------------------------------------"""


class CustomerViewSet(viewsets.ModelViewSet): # просмотр клиентов, редактирование админом
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerAPIView(APIView): # просмотр клиентов админом
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def get(self, request):
        customers = Customer.objects.all()
        return Response({'customers': CustomerSerializer(customers, many=True).data})


class CityViewSet(viewsets.ModelViewSet): # просмотр городов, редактирование админом
    permissions = (IsAuthenticatedOrReadOnly, )
    queryset = City.objects.all()
    serializer_class = CitySerializer

