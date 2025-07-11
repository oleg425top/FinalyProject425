from django.urls import path
from . import views
from .apps import PaymentsConfig
from .views import ProcessPaymentView, PaymentSuccessView

app_name = PaymentsConfig.name

"""Модуль URL-маршрутов для приложения платежей."""
urlpatterns = [
    path('pay/<int:order_id>/', ProcessPaymentView.as_view(), name='process_payment'),
    path('success/', PaymentSuccessView.as_view(), name='payment_success'),
]
