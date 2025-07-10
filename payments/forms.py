from django import forms

from users.forms import StyleFormMixin


class PaymentForm(StyleFormMixin, forms.Form):
    card_number = forms.CharField(label="Номер карты", max_length=16)
    expiry_date = forms.CharField(label="Срок действия", max_length=5)
    cvv = forms.CharField(label="CVV", max_length=4)
