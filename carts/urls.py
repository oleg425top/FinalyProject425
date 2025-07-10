from django.urls import path

from carts.apps import CartsConfig
from carts.views import UserCartView, CartAddView, CartRemoveView

"""Модуль URL-маршрутов для приложения корзины."""
app_name = CartsConfig.name

urlpatterns = [
    path('cart_add/<slug:slug>/', CartAddView.as_view(), name='cart_add'),
    path('user_cart/', UserCartView.as_view(), name='cart'),
    # path ('cart_change/<slug:slug>/', views.cart_change, name= 'cart_change'),
    path('cart_remove/<int:id>/', CartRemoveView.as_view(), name='cart_remove'),
]
