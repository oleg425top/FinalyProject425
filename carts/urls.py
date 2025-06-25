from django.urls import path

from carts import views
from carts.views import UserCartView

app_name = 'carts'

urlpatterns = [
    path ('cart_add/<slug:slug>/', views.cart_add, name= 'cart_add'),
    path ('user_cart/', UserCartView.as_view(), name= 'cart'),
    # path ('cart_change/<slug:slug>/', views.cart_change, name= 'cart_change'),
    # path ('cart_remove/<slug:slug>/', views.cart_remove, name= 'cart_remove'),
]