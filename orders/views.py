from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from users.services import send_order_email


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
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

                        messages.success(request, 'Заказ оформлен!')
                        send_order_email(user.email)
                        return redirect('users:profile')
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('orders:create_order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'phone_number': request.user.phone,
            'email': request.user.email,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - Оформление заказа',
        'form': form,
        'order': True,
    }
    return render(request, 'orders/create_order.html', context=context)
