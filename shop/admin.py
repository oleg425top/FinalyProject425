from django.contrib import admin

from shop.models import Brand, Tool


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Административный интерфейс для управления брендами."""
    list_display = ('name', 'description', 'logo')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    """Административный интерфейс для управления инструментами."""
    list_display = ('brand', 'name', 'description', 'price', 'quantity', 'discount',)
    list_filter = ('brand', 'discount',)
    list_editable = ('discount',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description',)
    fields = [
        'name',
        'brand',
        'slug',
        'description',
        ('price', 'discount'),
        'quantity',
    ]
