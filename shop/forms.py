from django import forms

from shop.models import Brand, Tool
from users.forms import StyleFormMixin


class BrandForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class ToolForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'