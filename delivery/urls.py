from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from customers import views
from delivery import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("api/v1/", include('user.urls')), # login/, user_list/, logout/, customer_register/, restaurant_register/
    path("api/v1/", include('restaurants.urls')),
    path("api/v1/", include('baskets.urls')),
    path("api/v1/", include('orders.urls')),
    path("api/v1/", include('customers.urls')),
    path("api/v1/", include('couriers.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)