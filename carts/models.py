from django.db import models

from shop.models import Tool
from users.models import User


class CartQueryset(models.QuerySet):
    """Набор запросов для модели Cart, предоставляющий методы для расчета общей стоимости и количества товаров."""

    def total_price(self):
        """Возвращает общую стоимость всех товаров в корзинах."""
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        """Возвращает общее количество товаров в корзинах."""
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    """Модель корзины, представляющая товары, добавленные пользователем."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = "Корзину"
        verbose_name_plural = "Корзины"
        ordering = ("id",)

    objects = CartQueryset.as_manager()

    def products_price(self):
        """Возвращает общую стоимость товаров в корзине с учетом количества."""
        return round(self.tool.sell_price() * self.quantity, 2)

    def __str__(self):
        """Возвращает строковое представление корзины с информацией о пользователе, товаре и количестве."""
        if self.user:
            return f'Корзина {self.user.email}| Товар {self.tool.name}| Количество {self.quantity}'
        return f'Анонимная корзина: | Товар {self.tool.name} | Количество {self.quantity}'
