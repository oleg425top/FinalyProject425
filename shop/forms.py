from django import forms

from shop.models import Brand, Tool
from users.forms import StyleFormMixin


class BrandForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Brand
        exclude = ('slug',)

class ToolForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Tool
        exclude = ('slug',)

class ToolAdminForm(BrandForms):
    class Meta:
        model = Tool
        fields = '__all__'

class ToolAdminFormCreate(StyleFormMixin, forms.ModelForm):
    slug = forms.SlugField(max_length=20, initial='temp_slug', widget=forms.HiddenInput)

    class Meta:
        model = Tool
        fields = '__all__'