from django.db import models
from orders.models import Order


class Payment(models.Model):
    """Модель платежа, связанная с заказом, содержащая информацию о транзакции и статусе оплаты."""
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    is_successful = models.BooleanField(default=False, verbose_name="Успешно")
    transaction_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID транзакции")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        """Возвращает строковое представление платежа с указанием статуса."""
        return f"Оплата заказа №{self.order.pk} - {'Успешно' if self.is_successful else 'Неуспешно'}"
