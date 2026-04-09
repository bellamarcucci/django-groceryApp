from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
]