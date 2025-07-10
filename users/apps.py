from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Конфигурация приложения Django для модуля пользователей."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Пользователи'
