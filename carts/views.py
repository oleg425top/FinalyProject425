from django.shortcuts import redirect
from django.views.generic import TemplateView

from carts.models import Cart
from shop.models import Tool


class UserCartView(TemplateView):
    """Отображает страницу корзины пользователя."""
    template_name = 'carts/cart.html'

    def get_context_data(self, **kwargs):
        """Добавляет данные в контекст для отображения на странице корзины."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Корзина'
        return context


def cart_add(request, slug):
    """
        Добавляет товар в корзину пользователя.

        Если пользователь аутентифицирован, увеличивает количество товара в корзине.
        Если товара нет в корзине, создает новую запись в корзине.

        Args:
            request: Объект запроса.
            slug: Slug товара для добавления в корзину.

        Returns:
            Перенаправляет на предыдущую страницу.
        """
    tool = Tool.objects.get(slug=slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, tool=tool)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, tool=tool, quantity=1)

    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, id):
    """
        Удаляет товар из корзины пользователя.

        Args:
            request: Объект запроса.
            id: Идентификатор записи корзины для удаления.

        Returns:
            Перенаправляет на предыдущую страницу.
        """
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
