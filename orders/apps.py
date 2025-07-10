from django.apps import AppConfig


class OrdersConfig(AppConfig):
    """Конфигурация приложения Django для модуля заказов."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = 'Заказы'
