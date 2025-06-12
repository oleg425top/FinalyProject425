from django.urls import path
from users.apps import UsersConfig
from users.views import index_view, UserRegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('', index_view, name='index'),
    path('users/register/', UserRegisterView.as_view(), name='register'),
]