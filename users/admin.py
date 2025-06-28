from django.contrib import admin
from users.models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'role', 'is_active')
    list_filter = ('first_name',)
    search_fields = ('email',)


