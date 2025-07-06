from django.conf import settings
from django.core.mail import send_mail


def send_register_email(email):
    send_mail(
        subject='Поздравляем с регистрацией на нашем сервисе',
        message='Вы успешно зарегистрировались в нашем магазине Электроинструмента!! Спасибо ',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ]
    )


def send_order_email(email):
    send_mail(
        subject='Поздравляем c оформлением заказа',
        message='Вы успешно оформили заказ на нашем сайте ',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ]
    )
