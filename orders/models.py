from django.db import models

from shop.models import Tool
from users.models import User


class OrderItemQueryset(models.QuerySet):
    """Набор запросов для модели OrderItem, предоставляющий методы для расчета общей стоимости и количества товаров."""

    def total_price(self):
        """Возвращает общую стоимость всех товаров в заказе."""
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        """Возвращает общее количество товаров в заказе."""
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    """Модель заказа, содержащая информацию о пользователе и деталях заказа."""
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Пользователь",
                             default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки")
    payment_on_get = models.BooleanField(default=False, verbose_name="Оплата при получении")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default='В обработке', verbose_name="Статус заказа")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ("id",)

    def __str__(self):
        """Возвращает строковое представление заказа."""
        return f"Заказ № {self.pk} | Покупатель {self.user.username} {self.user.email}"


class OrderItem(models.Model):
    """Модель элемента заказа, содержащая информацию о товаре и его количестве."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    tool = models.ForeignKey(Tool, on_delete=models.SET_DEFAULT, null=True, verbose_name="Продукт",
                             default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    class Meta:
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"
        ordering = ("id",)

    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        """Возвращает общую стоимость товаров в элементе заказа с учетом количества."""
        return round(self.price * self.quantity, 2)

    def __str__(self):
        """Возвращает строковое представление элемента заказа."""
        return f"Товар {self.name} | Заказ № {self.order.pk}"
