from django.contrib import admin

from shop.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo')
    list_filter = ('name',)
