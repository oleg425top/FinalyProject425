from django import forms
from django.contrib.auth.password_validation import validate_password

from users.models import User

# from users.validator import validate_password
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


class StyleFormMixin:
    """Миксин для стилизации форм, добавляющий CSS-класс 'form-control' ко всем полям формы."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, forms.ModelForm):
    """Форма для редактирования информации пользователя."""

    class Meta:
        model = User
        fields = ('email', 'first_name', 'phone',)


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма для регистрации нового пользователя."""

    class Meta:
        model = User
        fields = ('email',)


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    """Форма для аутентификации пользователя."""
    pass


class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    """Форма для обновления информации пользователя."""

    class Meta:
        model = User
        fields = ('email', 'first_name', 'phone',)


class UserChangePasswordForm(StyleFormMixin, PasswordChangeForm):
    """Форма для изменения пароля пользователя с валидацией."""

    def clean_new_password2(self):
        """Валидация нового пароля и проверка на совпадение паролей."""
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        validate_password(password1)
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch'
            )
        password_validation.validate_password(password2, self.user)
        return password2
