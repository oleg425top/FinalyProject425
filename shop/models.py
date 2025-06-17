from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='brand_name')
    description = models.TextField(blank=True, null=True, verbose_name='description')
    logo = models.ImageField(upload_to='brand_logos/', verbose_name='brand_logo')  # Поле для логотипа

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'
