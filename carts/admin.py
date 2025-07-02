from django.contrib import admin

from carts.models import Cart


# admin.site.register(Cart)

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "tool", "quantity", "created_timestamp"
    search_fields = "tool", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'tool_display', 'quantity', 'created_timestamp', ]
    list_filter = ['created_timestamp', 'user', 'tool__name', ]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимус"

    def tool_display(self, obj):
            return str(obj.tool.name)