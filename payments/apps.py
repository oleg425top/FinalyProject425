from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    """Конфигурация приложения Django для модуля платежей."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'
    verbose_name = 'Платежи'
