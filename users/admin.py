from django.contrib import admin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabularAdmin
from users.models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Административный интерфейс для управления пользователями."""
    list_display = ('pk', 'email', 'first_name', 'role', 'is_active')
    list_filter = ('first_name',)
    search_fields = ('email',)

    inlines = [CartTabAdmin, OrderTabularAdmin]
