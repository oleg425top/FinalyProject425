from django.conf import settings
from django.core.mail import send_mail


def send_register_email(email):
    """
    Отправляет электронное письмо с поздравлением по случаю успешной регистрации.

    Args:
        email (str): Адрес электронной почты получателя.
    """
    send_mail(
        subject='Поздравляем с регистрацией на нашем сервисе',
        message='Вы успешно зарегистрировались в нашем магазине Электроинструмента!! Спасибо ',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ]
    )


def send_new_password(email):
    send_mail(
        subject='Вы успешно изменили пароль',
        message=f'Ваш пароль был изменен',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ]
    )


def send_order_email(email):
    """
        Отправляет электронное письмо с подтверждением оформления заказа.

        Args:
            email (str): Адрес электронной почты получателя.
        """
    send_mail(
        subject='Поздравляем c оформлением заказа',
        message='Вы успешно оформили заказ на нашем сайте ',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ]
    )
