from django.urls import path
from .views import *

urlpatterns = [
    path('products_list/', ProductListCreateAPIView.as_view()),
    path('products_update/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('products_detail/<int:pk>/', ProductAPIDetailView.as_view(), name='detail'),
    path('products/', CreateProductAPIView.as_view(), name='create'),
]
