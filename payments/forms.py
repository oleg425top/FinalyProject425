from django import forms
from django.forms import TextInput

from users.forms import StyleFormMixin
from payments.card_validator import validate_card_number, validate_expiry_date, validate_cvv


class PaymentForm(StyleFormMixin, forms.Form):
    """Форма для ввода платежных данных, включая номер карты, срок действия и CVV."""
    card_number = forms.CharField(
        label="Номер карты", max_length=16,
        validators=[validate_card_number],
        widget=TextInput(attrs={'placeholder': '1234 5678 9012 3456'})
    )
    expiry_date = forms.CharField(
        label="Срок действия", max_length=5,
        validators=[validate_expiry_date],
        widget=TextInput(attrs={'placeholder': 'MM/YY'})
    )
    cvv = forms.CharField(
        label="CVV", max_length=4,
        validators=[validate_cvv],
        widget=TextInput(attrs={'placeholder': '123'})
    )
