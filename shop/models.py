

from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название брэнда')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    logo = models.ImageField(upload_to='brand_logos/', verbose_name='Логотип')
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'


class Tool(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Модель')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='tool_image/', blank=True, null=True, verbose_name='Фото инструмента')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Брэнд')

    def __str__(self):
        return f'({self.name}.Количество: {self.quantity}'

    def get_absolute_url(self):
        return reverse('shop:tool_detail', kwargs={"slug":self.slug})

    def display_id(self):
        return f'Арт: {self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'
