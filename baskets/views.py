from restaurants.models import Products
from baskets.models import Basket, Basket_product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from baskets.serializers import BasketProductSerializer, BasketSerializer
from user.permissions import IsCustomer
from .utils import StatusBasket
from django.db import transaction


class AddToBasketProductAPIView(APIView): # добавление продукта в корзину
    permission_classes = [IsCustomer]

    def post(self, request):
        product_id = request.data.get('product_id')
        basket_status = StatusBasket.LOADING

        try:
            basket = request.user.customer.basket_set.get(status=basket_status)
        except Basket.DoesNotExist:
            basket = Basket.objects.create(customer=request.user.customer, total=0, status=basket_status)

        try:
            product = Products.objects.get(pk=product_id)
        except Products.DoesNotExist:
            return Response({"error": "Продукт не существует"}, status=status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            basket_product, created = Basket_product.objects.get_or_create(
                basket=basket,
                product=product,
                defaults={'total': product.price, 'quantity': 1}
            )

            if not created:
                basket_product.quantity += 1
                basket_product.total = basket_product.quantity * product.price
                basket_product.save()

            basket.total = sum(item.total for item in basket.basket_product_set.all())
            basket.save()

        serializer = BasketProductSerializer(basket_product)
        return Response({"message": f"Продукт '{product.name}' добавлен", "data": serializer.data}, status=status.HTTP_201_CREATED)


class ListBasketProduct(APIView): # просмотр корзины продуктов пользователем
    permission_classes = [IsCustomer]

    def get(self, request, pk):
        try:
            instance = Basket_product.objects.get(pk=pk)
            serializer = BasketProductSerializer(instance)
            return Response(serializer.data)
        except Basket_product.DoesNotExist:
            return Response({'error': 'Корзина продуктов не существует'}, status=status.HTTP_404_NOT_FOUND)


class ListBasket(APIView): # просмотр корзины пользователем
    permission_classes = [IsCustomer]

    def get(self, request, pk):
        try:
            instance = Basket.objects.get(pk=pk)
            serializer = BasketSerializer(instance)
            return Response(serializer.data)
        except Basket.DoesNotExist:
            return Response({'error': 'Корзина не найдена'}, status=status.HTTP_404_NOT_FOUND)


class DeleteProductInBasketProduct(APIView): # удаление продукта из корзины
    permission_classes = [IsCustomer]

    def delete(self, request, pk):
        try:
            product = Products.objects.get(pk=pk)

            basket = request.user.customer.basket_set.get(status=StatusBasket.LOADING)

            basket_product = basket.basket_product_set.get(product=product)

            if basket_product.quantity > 1:
                basket_product.quantity -= 1
                basket_product.total -= product.price
                basket_product.save()
                basket.total -= product.price
                basket.save()

            else:
                basket_product.delete()
                basket.total -= product.price
                basket.save()

            return Response({"message": f"Продукт '{product.name}' удален из корзины."}, status=status.HTTP_204_NO_CONTENT)

        except Products.DoesNotExist:
            return Response({"message": "Продукт не существует."}, status=status.HTTP_404_NOT_FOUND)
        except Basket.DoesNotExist:
            return Response({"message": "Корзина не существует."}, status=status.HTTP_404_NOT_FOUND)
        except Basket_product.DoesNotExist:
            return Response({"message": "Продукт не найден в корзине."}, status=status.HTTP_404_NOT_FOUND)





