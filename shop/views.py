from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Brand


class BrandListView(ListView):
    model = Brand
    extra_context = {
        'title': 'Все наши породы'
    }
    template_name = 'shop/brands.html'
    paginate_by = 3
