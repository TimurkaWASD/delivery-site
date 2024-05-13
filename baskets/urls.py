from django.urls import path
from baskets.views import AddToBasketProductAPIView, ListBasketProduct, ListBasket, DeleteProductInBasketProduct

urlpatterns = [
    path('add_to_basket/', AddToBasketProductAPIView.as_view()),
    path('list_basket-product/<int:pk>', ListBasketProduct.as_view()),
    path('list_basket/<int:pk>', ListBasket.as_view()),
    path('delete_product/<int:pk>', DeleteProductInBasketProduct.as_view()),
    ]