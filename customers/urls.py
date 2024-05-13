from django.urls import path
from .views import *

urlpatterns = [
    path('add_customer_address/', AddCustomerAddressAPIView.as_view(), name='list'),
    path('add_customer_card/', AddCustomerCardAPIView.as_view(), name='')
]
