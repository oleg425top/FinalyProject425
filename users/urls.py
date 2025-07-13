from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page
from users.apps import UsersConfig
from users.views import UserRegisterView, UserLogoutView, UserLoginView, UserProfileView, UserUpdateView, \
    UserPasswordChangeView, IndexView, ContactsView, privacy_policy_view

"""Модуль URL-маршрутов для приложения пользователей."""

app_name = UsersConfig.name

urlpatterns = [path('', cache_page(1)(IndexView.as_view()), name='index'),
               path('contacts/', ContactsView.as_view(), name='contacts'),
               path('users/register/', UserRegisterView.as_view(), name='register'),
               path('users/logout/', UserLogoutView.as_view(), name='logout'),
               path('users/login/', UserLoginView.as_view(), name='login'),
               path('users/profile/', UserProfileView.as_view(), name='profile'),
               path('users/update/', UserUpdateView.as_view(), name='update'),
               path('users/change_password/', UserPasswordChangeView.as_view(), name='change_password'),
               path('privacy-policy/', privacy_policy_view, name='privacy_policy'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
