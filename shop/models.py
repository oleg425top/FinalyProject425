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
