from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from orders.models import Order
from .models import Payment
from .forms import PaymentForm


def payment_success(request):
    return render(request, 'payments/payment_success.html')


def process_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = Payment.objects.create(
                order=order,
                amount=sum([item.products_price() for item in order.orderitem_set.all()]),
                is_successful=True,
                transaction_id="TXN1234567890",
            )
            order.is_paid = True
            order.status = 'Оплачено'

            order.save()
            return redirect('payments:payment_success')
    else:
        form = PaymentForm()

    return render(request, "payments/payment_form.html", {"form": form, "order": order})
