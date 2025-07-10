from django.urls import path
from . import views
from .apps import PaymentsConfig

app_name = PaymentsConfig.name
urlpatterns = [
    path('pay/<int:order_id>/', views.process_payment, name='process_payment'),
    path('success/', views.payment_success, name='payment_success'),
]
