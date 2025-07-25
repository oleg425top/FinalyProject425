import re
from django import forms


class CreateOrderForm(forms.Form):
    """Форма для создания заказа с валидацией данных."""

    first_name = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
    )

    def clean_phone_number(self):
        """Валидация номера телефона: проверка на цифры и соответствие формату."""
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")

        pattern = re.compile(r'^\d{11}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data
