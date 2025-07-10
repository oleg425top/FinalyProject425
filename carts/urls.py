from django.urls import path

from carts import views
from carts.apps import CartsConfig
from carts.views import UserCartView

"""Модуль URL-маршрутов для приложения корзины."""
app_name = CartsConfig.name

urlpatterns = [
    path('cart_add/<slug:slug>/', views.cart_add, name='cart_add'),
    path('user_cart/', UserCartView.as_view(), name='cart'),
    # path ('cart_change/<slug:slug>/', views.cart_change, name= 'cart_change'),
    path('cart_remove/<int:id>/', views.cart_remove, name='cart_remove'),
]
