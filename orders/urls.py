from django.urls import path

from orders import views
from orders.apps import OrdersConfig

app_name = OrdersConfig.name

urlpatterns = [
    # path('create_order/', views.CreateOrderView.as_view(), name='create_order'),
    path('create_order/', views.create_order, name='create_order'),
]