from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a customer

        return request.user.is_authenticated and hasattr(request.user, 'customer')

class IsRestaurant(BasePermission):

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a restaurant
        return request.user.is_authenticated and hasattr(request.user, 'restaurant')