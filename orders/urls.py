from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('checkout/', views.checkout_cart, name='checkout_cart'),
    path('manage/', views.manage_orders, name='manage_orders'),
    path('approve/<int:order_id>/', views.approve_order, name='approve_order'),
    path('deny/<int:order_id>/', views.deny_order, name='deny_order'),
]