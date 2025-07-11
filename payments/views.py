from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView

from orders.models import Order
from .models import Payment
from .forms import PaymentForm


class PaymentSuccessView(TemplateView):
    """Отображает страницу успешного завершения платежа."""
    template_name = 'payments/payment_success.html'


class ProcessPaymentView(FormView):
    """
    Обрабатывает платеж для заказа с указанным идентификатором.
    Если запрос POST, валидирует форму платежа и создает запись платежа.
    Обновляет статус заказа на 'Оплачено' и перенаправляет на страницу успешного платежа.
    """
    template_name = "payments/payment_form.html"
    form_class = PaymentForm

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного платежа."""
        return reverse_lazy('payments:payment_success')

    def get_form_kwargs(self):
        """Добавляет заказ в контекст формы."""
        kwargs = super().get_form_kwargs()
        return kwargs

    def get_order(self):
        """Получает заказ по идентификатору."""
        return get_object_or_404(Order, id=self.kwargs['order_id'])

    def form_valid(self, form):
        """Обрабатывает валидную форму, создавая платеж и обновляя заказ."""
        order = self.get_order()
        payment = Payment.objects.create(
            order=order,
            amount=sum([item.products_price() for item in order.orderitem_set.all()]),
            is_successful=True,
            transaction_id="TXN1234567890",
        )
        order.is_paid = True
        order.status = 'Оплачено'
        order.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Добавляет заказ в контекст для отображения на странице формы платежа."""
        context = super().get_context_data(**kwargs)
        context['order'] = self.get_order()
        return context
