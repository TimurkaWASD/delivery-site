from baskets.utils import StatusBasket
from couriers.permissions import IsCourier
from orders.utils import PaymentMethod
from restaurants.models import Restaurant
from orders.models import Order, Payment_method, Delivery
from rest_framework.views import APIView, status
from rest_framework.response import Response
from orders.serializers import OrderSerializer, UpdateOrderStatusSerializer, UpdateDeliveryStatusSerializer, \
    ReviewOrdersSerializer
from django.utils import timezone
from user.permissions import IsRestaurant, IsCustomer


class OrderCreateAPIView(APIView): # создание заказа клиентом
    permission_classes = [IsCustomer]

    def post(self, request):
        user = request.user
        customer = user.customer

        basket = customer.basket_set.filter(status=StatusBasket.LOADING).first()
        if not basket:
            return Response({'error': 'Наполненной корзины не найдено'}, status=status.HTTP_400_BAD_REQUEST)

        total_amount = basket.total
        request.data['total_amount'] = total_amount


        basket_product = basket.basket_product_set.first()
        if not basket_product:
            return Response({'error': 'Корзина пуста'}, status=status.HTTP_400_BAD_REQUEST)

        product = basket_product.product
        restaurant = product.restaurant

        order_datetime = timezone.now()

        order = Order.objects.create(
            basket=basket,
            total_amount=total_amount,
            restaurant=restaurant,
            customer=customer,
            order_datetime=order_datetime
        )

        basket.status = StatusBasket.FILLED
        basket.save()

        serializer = OrderSerializer(order)

        """
        {
            none
        }
        """

        return Response({"message": "Заказ создан", "data": serializer.data}, status=status.HTTP_201_CREATED)



class RestaurantOrderListView(APIView): # просмотр заказов рестораном
    permissions_class = [IsRestaurant]
    def get(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({"error": "Ресторан не найден"}, status=status.HTTP_404_NOT_FOUND)

        orders = Order.objects.filter(restaurant=restaurant)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateOrderStatusAPIView(APIView): # обновление статус заказа рестораном
    permissions_class = [IsRestaurant]
    def post(self, request):
        serializer = UpdateOrderStatusSerializer(data=request.data)
        if serializer.is_valid():
            order_id = serializer.validated_data['order_id']
            new_status = serializer.validated_data['new_status']

            order = Order.objects.get(id=order_id)
            order.status = new_status
            order.save()

            """
            {
                "order_id": 1,
                "new_status": 1
            }
            """

            return Response("Статус заказа был обновлен", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CreatePaymentMethodAPIView(APIView): # создание и выбор метода оплаты клиентом
    permissions_class = [IsCustomer]
    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Заказ не найден'}, status=status.HTTP_404_NOT_FOUND)

        payment_methods = request.data.get('payment_methods')
        if payment_methods not in [PaymentMethod.CREDIT_CARD, PaymentMethod.CASH_PAYMENT]:
            return Response({'error': 'Неверный способ оплаты'}, status=status.HTTP_400_BAD_REQUEST)

        payment_datetime = timezone.now()

        payment_method = Payment_method.objects.create(
            order=order,
            payment_datetime=payment_datetime,
            payment_methods=payment_methods,
        )

        """
        {
            "payment_methods": 1
        }
        """

        return Response({'success': 'Способ оплаты успешно создан'}, status=status.HTTP_201_CREATED)

class CreateDeliveryAPIView(APIView): # создание доставки клиентом
    permission_classes = [IsCustomer]

    def post(self, request, order_id):
        user = request.user
        customer = user.customer

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Заказ не найден'}, status=status.HTTP_404_NOT_FOUND)

        delivery_datetime = timezone.now()
        start_order_datetime = timezone.now()
        end_order_datetime = timezone.now()

        """
        start_order_datetime = request.data.get('start_order_datetime')
        end_order_datetime = request.data.get('end_order_datetime')

        # Проверяем, что все параметры времени были предоставлены
        if not (start_order_datetime and end_order_datetime):
            return Response({'error': 'Необходимо предоставить все параметры времени'}, status=status.HTTP_400_BAD_REQUEST)
            
        {
            "start_order_datetime": "2024-04-04T14:00:00",
            "end_order_datetime": "2024-04-04T16:00:00"
        }
        """


        delivery = Delivery.objects.create(
            order=order,
            delivery_datetime=delivery_datetime,
            start_order_datetime=start_order_datetime,
            end_order_datetime=end_order_datetime,
        )

        """
        {
            none
        }
        """

        return Response({'success': 'Доставка создана'}, status=status.HTTP_201_CREATED)

class UpdateDeliveryStatusAPIView(APIView): # обновление статуса доставкии
    permissions_class = [IsCourier]

    def post(self, request):
        serializer = UpdateDeliveryStatusSerializer(data=request.data)
        if serializer.is_valid():
            delivery_id = serializer.validated_data.get('delivery_id')
            new_status = serializer.validated_data.get('new_status')

            if Delivery.objects.filter(id=delivery_id).exists():
                delivery = Delivery.objects.get(id=delivery_id)
                delivery.status = new_status
                delivery.save()

                """
                {
                    "order": 9,
                    "delivery_id": 5,
                    "new_status": 3
                }
                """

                return Response("Статус доставки был обновлен", status=status.HTTP_200_OK)
            else:
                return Response("Доставка не найдена", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeliveryTimeAPIView(APIView): # обновление времени доставки курьером
    permission_classes = [IsCourier]
    def patch(self, request, delivery_id):
        try:
            delivery = Delivery.objects.get(id=delivery_id)
        except Delivery.DoesNotExist:
            return Response({'error': 'Доставка не найдена'}, status=status.HTTP_404_NOT_FOUND)

        delivery_datetime = request.data.get('delivery_datetime')
        start_order_datetime = request.data.get('start_order_datetime')
        end_order_datetime = request.data.get('end_order_datetime')

        if delivery_datetime:
            delivery.delivery_datetime = delivery_datetime
        if start_order_datetime:
            delivery.start_order_datetime = start_order_datetime
        if end_order_datetime:
            delivery.end_order_datetime = end_order_datetime

        delivery.save()

        """
        {
            "delivery_datetime": "2024-04-04T15:30:00",
            "start_order_datetime": "2024-04-04T14:00:00",
            "end_order_datetime": "2024-04-04T16:30:00"
        }
        """

        return Response({'success': 'Время доставки успешно обновлено'}, status=status.HTTP_200_OK)

class UpdatePaymentMethodAPIView(APIView): # обновление метода оплаты заказчиком
    permission_classes = [IsCustomer]

    def patch(self, request, payment_method_id):
        try:
            payment_method = Payment_method.objects.get(id=payment_method_id)
        except Payment_method.DoesNotExist:
            return Response({'error': 'Платеж не найден'}, status=status.HTTP_404_NOT_FOUND)

        new_payment_method_value = request.data.get('payment_method_value')
        if new_payment_method_value is None:
            return Response({'error': 'Отсутствует новое значение метода оплаты'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_payment_method = PaymentMethod(new_payment_method_value)
        except ValueError:
            return Response({'error': 'Неверное значение метода оплаты'}, status=status.HTTP_400_BAD_REQUEST)

        payment_method.payment_methods = new_payment_method.value
        payment_method.save()

        """
        {
            "payment_method_value": 1 or 2
        }
        """

        return Response({'success': 'Способ оплаты успешно изменен'}, status=status.HTTP_200_OK)

class ReviewOrdersAPIView(APIView):
    permission_classes = [IsCustomer]
    def post(self, request):
        serializer = ReviewOrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


