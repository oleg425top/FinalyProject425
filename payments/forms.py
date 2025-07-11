from django import forms
from django.forms import TextInput

from users.forms import StyleFormMixin


class PaymentForm(StyleFormMixin, forms.Form):
    """Форма для ввода платежных данных, включая номер карты, срок действия и CVV."""
    card_number = forms.CharField(
        label="Номер карты", max_length=16,
        widget=TextInput(attrs={'placeholder': '1234 5678 9012 3456'})
    )
    expiry_date = forms.CharField(
        label="Срок действия", max_length=5,
        widget=TextInput(attrs={'placeholder': 'MM/YY'})
    )
    cvv = forms.CharField(
        label="CVV", max_length=4,
        widget=TextInput(attrs={'placeholder': '123'})
    )
