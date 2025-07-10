from django.apps import AppConfig


class ShopConfig(AppConfig):
    """Конфигурация приложения Django для модуля магазина."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
    verbose_name = 'магазин'
