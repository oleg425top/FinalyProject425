from django.urls import path

from orders import views
from orders.apps import OrdersConfig

"""Модуль URL-маршрутов для приложения заказов."""
app_name = OrdersConfig.name

urlpatterns = [
    path('create_order/', views.CreateOrderView.as_view(), name='create_order'),
    path('statistics/', views.order_statistics, name='order_statistics'),
]
