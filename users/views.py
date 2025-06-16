from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from users.models import User
from users.forms import UserRegisterForm, UserLoginForm, UserForm, UserUpdateForm, UserChangePasswordForm


def index_view(request):
    return render(request, 'users/index.html')


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:index')
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Создать аккаунт'
    }


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    extra_context = {
        'title': 'Выход из аккаунта'
    }


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = ''
    extra_context = {
        'title': 'Вход в аккаунт'
    }


class UserProfileView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = f'Ваш профиль {self.get_object()}'
        return context_data

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = f'Обновить профиль {self.get_object()}'
        return context_data

class UserPasswordChangeView(PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = f'Изменить пароль {self.request.user}'
        return context_data
