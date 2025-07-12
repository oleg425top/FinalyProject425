from django import template

from orders.models import Order

register = template.Library()


@register.simple_tag()
def user_orders(request):
    if request.user.is_authenticated:
        return Order.objects.filter(user=request.user)
