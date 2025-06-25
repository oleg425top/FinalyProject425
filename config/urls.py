from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('users.urls', namespace='users')),
                path('shop/', include('shop.urls', namespace='shop')),
                path('cart/', include('carts.urls', namespace='cart')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
