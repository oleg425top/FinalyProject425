from django.urls import path
from users.apps import UsersConfig
from users.views import index_view

app_name = UsersConfig.name

urlpatterns = [
    path('', index_view, name='index'),
]