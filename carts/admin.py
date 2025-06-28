from django.contrib import admin

from carts.models import Cart

# admin.site.register(Cart)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'tool', 'quantity', 'created_timestamp',]
    list_filter = ['created_timestamp', 'user', 'tool',]