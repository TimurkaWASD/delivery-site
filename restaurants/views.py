from user.permissions import IsRestaurant
from .models import Products, Categories, Restaurant
from .permissions import IsOwnerOrReadOnly
from .serializers import ProductSerializer, CategorySerializer, RestaurantSerializer, CreateProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView): # получение детали дродукта ресторана
    # queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsRestaurant]
    
    def get_queryset(self):
        # Получаем идентификатор ресторана из параметров запроса
        restaurant_id = self.request.user.restaurant.id
        # product = self.request.user.restaurant.products_set.get(pk=3)
        # product.name = "Пицца"
        # product.save()
        # Фильтруем продукты по идентификатору ресторана
        queryset = Products.objects.filter(pk=self.kwargs['pk'], restaurant_id = restaurant_id)
        return queryset

class CreateProductAPIView(generics.ListCreateAPIView): #
    serializer_class = CreateProductSerializer
    permission_classes = [IsRestaurant]

    def get_queryset(self):
        queryset = Products.objects.filter(restaurant_id=self.request.user.restaurant.id)
        return queryset

    def perform_create(self, serializer):
        # Set the restaurant ID for the created product
        serializer = CreateProductSerializer(data=self.request.data, context={'restaurant_id': self.request.user.restaurant.id})
        serializer.is_valid()
        serializer.save()



"""------------------------------------------------ api check -------------------------------------------------------"""
class ProductViewSet(viewsets.ModelViewSet):
    permissions_class = (IsOwnerOrReadOnly, )
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    permissions_class = (IsOwnerOrReadOnly, )
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permissions_class = (IsOwnerOrReadOnly, )
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

"""----------------------------------------- api restaurant create products -----------------------------------------"""
class ProductListCreateAPIView(generics.ListCreateAPIView):
    permissions_class = (IsAuthenticated, )
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permissions_class = (IsAuthenticated, )
    queryset = Products.objects.all()
    serializer_class = ProductSerializer




