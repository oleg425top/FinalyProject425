from django.contrib import admin

from shop.models import Brand, Tool


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'description', 'price')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
