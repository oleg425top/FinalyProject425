from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [

]