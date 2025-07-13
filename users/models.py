from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRolls(models.TextChoices):
    """Роли пользователей в системе."""
    ADMIN = 'admin', _('admin')
    MODERATOR = 'moderator', _('moderator')
    USER = 'user', _('user')


class User(AbstractUser):
    """Пользовательская модель, расширяющая базовую модель пользователя Django."""
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    role = models.CharField(max_length=9, choices=UserRolls.choices, default=UserRolls.USER, verbose_name='Статус')
    first_name = models.CharField(max_length=150, verbose_name='Имя', default='Аноним')
    phone = models.CharField(max_length=35, unique=True, verbose_name='phone', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """Возвращает строковое представление пользователя."""
        if self.first_name != 'Аноним':
            return f'{self.first_name}'
        else:
            return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']


class PrivacyPolicy(models.Model):
    """Модель для хранения текста политики конфиденциальности."""
    title = models.CharField(max_length=255, default="Политика конфиденциальности")
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Возвращает заголовок политики конфиденциальности."""
        return self.title

    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'
