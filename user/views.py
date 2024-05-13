from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from couriers.serializers import CourierSerializer
from customers.serializers import CustomerSerializer
from restaurants.serializers import RestaurantSerializer

from .models import CustomUser
from .serializers import CustomUserSerializer, BasketSerializer


class UserAPIList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomerRegistrationAPIView(APIView):
    def post(self, request):
        user_serializer = CustomUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            customer_data = {
                'user': user.id,
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
            }
            customer_serializer = CustomerSerializer(data=customer_data)
            if customer_serializer.is_valid():
                customer = customer_serializer.save()

                basket_data = {
                    'customer': customer.id,
                    'total': 0,
                    'status': 1,
                }
                basket_serializer = BasketSerializer(data=basket_data)
                if basket_serializer.is_valid():
                    basket = basket_serializer.save()
                else:
                    customer.delete()  # Rollback customer creation if basket creation fails
                    user.delete()  # Rollback user creation if customer creation fails
                    return Response(basket_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.delete()  # Rollback user creation if customer creation fails
                return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class RestaurantRegistrationAPIView(APIView):
    def post(self, request):
            # Serialize user data
            user_serializer = CustomUserSerializer(data=request.data)
            
            if user_serializer.is_valid():
                # Save user
                user = user_serializer.save()
                # Generate token
                token, created = Token.objects.get_or_create(user=user)
                
                # Serialize restaurant data
                restaurant_data = {
                    'user': user.id,
                    'name': request.data.get('restaurant_name'),  # Adjust according to your input data
                    'description': request.data.get('description'),
                    'address': request.data.get('address'),
                    'rating': request.data.get('rating'),
                    'image': request.data.get('image'),  # Adjust according to your input data
                    'is_work': request.data.get('is_work'),
                    'city': request.data.get('city')  # Adjust according to your input data
                }
                restaurant_serializer = RestaurantSerializer(data=restaurant_data)
                
                if restaurant_serializer.is_valid():
                    # Save restaurant
                    restaurant_serializer.save()
                    return Response({'token': token.key}, status=status.HTTP_201_CREATED)
                else:
                    # Rollback user creation if restaurant creation fails
                    user.delete()
                    return Response(restaurant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    






class LoginAPIView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number', '')
        password = request.data.get('password', '')

        user = CustomUser.objects.filter(phone_number=phone_number).first()

        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

class CourierRegistrationAPIView(APIView):
    def post(self, request):
        user_serializer = CustomUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            customer_data = {
                            'user': user.id,
                            'first_name': request.data.get('first_name'),
                            'last_name': request.data.get('status'),
                            'last_name': request.data.get('photo')
                            }
            courier_serializer = CourierSerializer(data=customer_data)
            if courier_serializer.is_valid():
                customer = courier_serializer.save()
            else:
                user.delete()  # Rollback user creation if customer creation fails
                return Response(courier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,}, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
