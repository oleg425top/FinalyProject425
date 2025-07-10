from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, View

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


class CartAddView(View):
    """
    Класс представления для добавления товара в корзину пользователя.
    Если пользователь аутентифицирован, увеличивает количество товара в корзине.
    Если товара нет в корзине, создает новую запись в корзине.
    """

    def get(self, request, slug):
        tool = get_object_or_404(Tool, slug=slug)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, tool=tool)
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, tool=tool, quantity=1)

        response_data = {
            "message": "Товар добавлен в корзину",
        }

        return redirect(request.META.get('HTTP_REFERER', '/'), response_data)


#
class CartRemoveView(View):
    """
    Класс представления для удаления товара из корзины пользователя.
    """

    def get(self, request, id):
        """
        Удаляет товар из корзины пользователя.

        Args:
            request: Объект запроса.
            id: Идентификатор записи корзины для удаления.

        Returns:
            Перенаправляет на предыдущую страницу.
        """
        cart = get_object_or_404(Cart, id=id)
        cart.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
