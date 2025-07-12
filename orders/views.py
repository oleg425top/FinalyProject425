from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Sum, F, Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from users.services import send_order_email


class CreateOrderView(LoginRequiredMixin, FormView):
    """ Представление для создания заказа. Требует авторизации пользователя."""
    template_name = 'orders/create_order.html'
    form_class = CreateOrderForm
    success_url = reverse_lazy('users:profile')

    def get_initial(self):
        """ Инициализирует форму начальными данными пользователя."""
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['email'] = self.request.user.email
        initial['phone_number'] = self.request.user.phone
        return initial

    def form_valid(self, form):
        """ Обрабатывает валидную форму, создавая заказ и очищая корзину."""
        try:
            with transaction.atomic():
                user = self.request.user
                cart_items = Cart.objects.filter(user=user)

                if cart_items.exists():
                    # Создать заказ
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=form.cleaned_data['requires_delivery'],
                        delivery_address=form.cleaned_data['delivery_address'],
                        payment_on_get=form.cleaned_data['payment_on_get'],
                    )
                    # Создать заказанные товары
                    for cart_item in cart_items:
                        tool = cart_item.tool
                        name = cart_item.tool.name
                        price = cart_item.tool.sell_price()
                        quantity = cart_item.quantity

                        if tool.quantity < quantity:
                            raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {tool.quantity}')

                        OrderItem.objects.create(
                            order=order,
                            tool=tool,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )
                        tool.quantity -= quantity
                        tool.save()
                    cart_items.delete()
                    messages.success(self.request, 'Заказ оформлен!')
                    send_order_email(user.email)
                    return redirect('users:profile')
        except ValidationError as e:
            messages.error(self.request, str(e))
            return redirect('orders:create_order')

    def form_invalid(self, form):
        """ Обрабатывает невалидную форму, выводя сообщение об ошибке."""
        messages.error(self.request, 'Заполните поля заново')
        return redirect('orders:create_order')

    def get_context_data(self, **kwargs):
        """ Добавляет данные в контекст для отображения на странице создания заказа."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление заказа'
        context['order'] = True
        return context


def order_statistics(request):
    """Собирает и возвращает статистику по заказам для отображения на сайте."""
    total_orders = Order.objects.count()
    paid_orders = Order.objects.filter(is_paid=True).count()
    unpaid_orders = Order.objects.filter(is_paid=False).count()
    total_sales = OrderItem.objects.aggregate(total=Sum(F('price') * F('quantity')))['total'] or 0

    top_products = (
        OrderItem.objects.values('name')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('-total_quantity')[:5]
    )

    with_delivery = Order.objects.filter(requires_delivery=True).count()
    without_delivery = Order.objects.filter(requires_delivery=False).count()

    delivery_stats = {
        'with_delivery': with_delivery,
        'without_delivery': without_delivery,
    }

    status_counts = (
        Order.objects
        .values('status')
        .annotate(count=Count('id'))
        .order_by()  # отменяем ordering из модели, чтобы избежать ошибки
    )

    context = {
        'total_orders': total_orders,
        'paid_orders': paid_orders,
        'unpaid_orders': unpaid_orders,
        'total_sales': total_sales,
        'top_products': top_products,
        'delivery_stats': delivery_stats,
        'status_counts': status_counts,
    }
    return render(request, 'orders/statistics.html', context)
