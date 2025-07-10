from django.apps import AppConfig


class CartsConfig(AppConfig):
    """Конфигурация приложения Django для модуля корзин."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carts'
    verbose_name = 'корзины'
