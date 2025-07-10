from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemTabularAdmin(admin.TabularInline):
    """Интерфейс для редактирования элементов заказа в виде таблицы."""
    model = OrderItem
    fields = "tool", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Административный интерфейс для управления элементами заказа."""
    list_display = "order", "tool", "name", "price", "quantity"
    search_fields = (
        "order",
        "tool",
        "name",
    )


class OrderTabularAdmin(admin.TabularInline):
    """Интерфейс для редактирования заказов в виде таблицы."""
    model = Order
    fields = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "requires_delivery",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Административный интерфейс для управления заказами."""
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "id",
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
    )
    inlines = (OrderItemTabularAdmin,)
