from django import forms

from shop.models import Brand
from users.forms import StyleFormMixin


class BrandForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'