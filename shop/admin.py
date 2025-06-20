from django.contrib import admin

from shop.models import Brand, Tool


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo')
    list_filter = ('name',)


@admin.register(Tool)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'price')
    list_filter = ('name',)