from django import forms

from shop.models import Brand, Tool
from users.forms import StyleFormMixin


class BrandForms(StyleFormMixin, forms.ModelForm):
    """Форма для работы с моделью Brand, исключая поле slug."""

    class Meta:
        model = Brand
        exclude = ('slug',)


class ToolForms(StyleFormMixin, forms.ModelForm):
    """Форма для работы с моделью Tool, исключая поле slug."""

    class Meta:
        model = Tool
        exclude = ('slug',)


class ToolAdminForm(BrandForms):
    """Форма администратора для работы со всеми полями модели Tool."""

    class Meta:
        model = Tool
        fields = '__all__'


class ToolAdminFormCreate(StyleFormMixin, forms.ModelForm):
    """Форма для создания нового инструмента, включающая скрытое поле slug."""
    slug = forms.SlugField(max_length=20, initial='temp_slug', widget=forms.HiddenInput)

    class Meta:
        model = Tool
        fields = '__all__'
