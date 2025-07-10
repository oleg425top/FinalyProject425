from django.contrib import admin

from carts.models import Cart


class CartTabAdmin(admin.TabularInline):
    """Интерфейс для редактирования корзины в контексте родительской модели."""
    model = Cart
    fields = "tool", "quantity", "created_timestamp"
    search_fields = "tool", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Настройка админ-интерфейса для модели корзины."""
    list_display = ['user_display', 'tool_display', 'quantity', 'created_timestamp', ]
    list_filter = ['created_timestamp', 'user', 'tool__name', ]

    def user_display(self, obj):
        """Отображает пользователя, связанного с корзиной, или 'Аноним' если пользователь не указан."""
        if obj.user:
            return str(obj.user)
        return "Анонимус"

    def tool_display(self, obj):
        """Отображает название инструмента, связанного с корзиной."""
        return str(obj.tool.name)

    user_display.short_description = "Пользователь"
    tool_display.short_description = "Товар"
