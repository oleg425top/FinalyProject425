from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, TemplateView, View
from django.urls import reverse_lazy

from users.models import User, PrivacyPolicy
from users.forms import UserRegisterForm, UserLoginForm, UserForm, UserUpdateForm, UserChangePasswordForm, ContactsForm
from users.services import send_register_email, send_new_password, send_message


class IndexView(TemplateView):
    """Отображает главную страницу магазина электроинструментов."""
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        """Добавляет данные в контекст для отображения на главной странице."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Магазин электроинструмента - главная'
        context['content'] = 'Магазин электроинструментов'
        return context


class ContactsView(View):
    """ Класс для обработки формы обратной связи. """
    template_name = 'users/contacts.html'
    form_class = ContactsForm

    def get(self, request, *args, **kwargs):
        """ Обрабатывает GET-запросы для отображения формы обратной связи. """
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """ Обрабатывает POST-запросы для отправки данных формы. """
        form = self.form_class(request.POST)
        if form.is_valid():
            send_message(
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['message']
            )
            return render(request, self.template_name, {'success': 1, 'form': form})
        return render(request, self.template_name, {'form': form})


class UserRegisterView(CreateView):
    """Представление для регистрации нового пользователя."""
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Создать аккаунт'
    }

    def form_valid(self, form):
        """Обрабатывает валидную форму регистрации и отправляет письмо с подтверждением."""
        self.object = form.save()
        send_register_email(self.object.email)
        messages.success(self.request, f'{self.object.email} вы успешно зарегистрировались!!')
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    """Представление для выхода пользователя из системы."""
    template_name = 'users/logout.html'
    extra_context = {
        'title': 'Выход из аккаунта'
    }

    def dispatch(self, request, *args, **kwargs):
        """Отправляет сообщение об успешном выходе из системы."""
        messages.success(request, f"{request.user.first_name}, Вы вышли из аккаунта")
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(LoginView):
    """Представление для входа пользователя в систему."""
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = ''
    extra_context = {
        'title': 'Вход в аккаунт'
    }


class UserProfileView(UpdateView):
    """Представление для отображения и редактирования профиля пользователя."""
    model = User
    form_class = UserForm
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        """Возвращает текущего пользователя для отображения его профиля."""
        return self.request.user

    def get_context_data(self, **kwargs):
        """Добавляет данные в контекст для отображения на странице профиля."""
        context_data = super().get_context_data()
        context_data['title'] = f'Ваш профиль {self.get_object()}'
        return context_data


class UserUpdateView(UpdateView):
    """Представление для обновления информации пользователя."""
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """Возвращает текущего пользователя для обновления его данных."""
        return self.request.user

    def get_context_data(self, **kwargs):
        """Добавляет данные в контекст для отображения на странице обновления профиля."""
        context_data = super().get_context_data()
        context_data['title'] = f'Обновить профиль {self.get_object()}'
        return context_data


class UserPasswordChangeView(PasswordChangeView):
    """Представление для изменения пароля пользователя."""
    form_class = UserChangePasswordForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        """Добавляет данные в контекст для отображения на странице изменения пароля."""
        context_data = super().get_context_data()
        context_data['title'] = f'Изменить пароль {self.request.user}'
        return context_data

    def form_valid(self, form):
        """ Проверяет форму на валидность. Сохраняет пользователя. Отправляет сообщение о смене пароля на почту."""
        user = form.save()
        send_new_password(user.email)
        return super().form_valid(form)


def privacy_policy_view(request):
    """Выводит страницу политики конфиденциальности."""
    policy = get_object_or_404(PrivacyPolicy)
    return render(request, 'users/privacy_policy.html', {'policy': policy})
