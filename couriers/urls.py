from django.urls import path
from .views import *

urlpatterns = [

    path('courier/order_list/', CourierOrdersListView.as_view(), name='orders'),
    path('courier/accept/', CourierDeliveryAcceptView.as_view(), name='accept'),
]