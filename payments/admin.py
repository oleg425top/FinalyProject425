from django.contrib import admin

from payments.models import Payment


@admin.register(Payment)
class CartAdmin(admin.ModelAdmin):
    """Настройка админ-интерфейса для модели корзины."""
    list_display = ['order', 'amount', 'is_successful', 'created_at', ]
    list_filter = ['created_at', ]
