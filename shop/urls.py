from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from shop.apps import ShopConfig
from shop.views import BrandListView, BrandCreateView, about_view, ToolListView, ToolCreateView, ToolDeleteView, \
    ToolUpdateView, BrandToolsListView

app_name = ShopConfig.name

urlpatterns = [
    path('about/', about_view, name='about'),
    path('catalog/brands/', cache_page(1)(BrandListView.as_view()), name='catalog'),

    path('catalog/brands/create/', BrandCreateView.as_view(), name='brand_create'),
    path('catalog/tools/', cache_page(1)(ToolListView.as_view()), name='tools'),
    path('catalog/tools/create', cache_page(1)(ToolCreateView.as_view()), name='tool_create'),
    path('catalog/tools/delete/<int:pk>/', cache_page(1)(ToolDeleteView.as_view()), name='tool_delete'),
    path('catalog/tools/update/<int:pk>/', cache_page(1)(ToolUpdateView.as_view()), name='tool_update'),
    path('catalog/brand/<int:pk>/tools/', cache_page(1)(BrandToolsListView.as_view()), name='brand_tool'),

]
