from django.urls import path
from couriers.views import CourierOrdersListView, CourierDeliveryAcceptView
from orders.views import *

urlpatterns = [
    path('create_order/', OrderCreateAPIView.as_view()),
    path('restaurant/<int:restaurant_id>/orders/', RestaurantOrderListView.as_view()),
    path('update-order-status/', UpdateOrderStatusAPIView.as_view(), name='update_order_status'),
    path('create_payment_method/<int:order_id>/', CreatePaymentMethodAPIView.as_view(), name='create_payment_method'),
    path('courier/order-list/', CourierOrdersListView.as_view(), name='orders'),
    path('courier/accept/',CourierDeliveryAcceptView.as_view(), name='accept'),
    path('create-delivery/<int:order_id>/', CreateDeliveryAPIView.as_view()),
    path('update-delivery-status/', UpdateDeliveryStatusAPIView.as_view(), name='update_delivery_status'),
    path('update_delivery_time/<int:delivery_id>/', UpdateDeliveryTimeAPIView.as_view()),
    path('review_orders/', ReviewOrdersAPIView.as_view(), name='review-orders'),
    path('update_payment_method/<int:payment_method_id>/', UpdatePaymentMethodAPIView.as_view())
]