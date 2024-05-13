from django.urls import path
from .views import *
app_name='user'
urlpatterns = [
    path('user_list/', UserAPIList.as_view(), name='list'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('customer_register/', CustomerRegistrationAPIView().as_view(), name='customer_register'),
    path('restaurant_register/', RestaurantRegistrationAPIView().as_view(), name='restaurant_register'),
    path('courier_register/', CourierRegistrationAPIView().as_view(), name='courier_register'),
]
