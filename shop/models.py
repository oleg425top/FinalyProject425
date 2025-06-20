from django.db import models


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
    name = models.CharField(max_length=100, unique=True, verbose_name='Название брэнда')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='tool_image/', blank=True, null=True, verbose_name='Фото инструмента')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'