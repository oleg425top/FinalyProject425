from datetime import datetime
import re

from django.core.exceptions import ValidationError


def validate_card_number(value):
    """Проверяет, что номер карты состоит из 16 цифр."""
    if not value.isdigit():
        raise ValidationError("Номер карты должен содержать только цифры.")
    if len(value) != 16:
        raise ValidationError("Номер карты должен содержать ровно 16 цифр.")


def validate_expiry_date(value):
    """Проверяет, что срок действия карты в формате MM/YY и не истёк."""
    if not re.match(r'^\d{2}/\d{2}$', value):
        raise ValidationError("Срок действия должен быть в формате MM/YY.")

    try:
        month, year = map(int, value.split('/'))
        if not 1 <= month <= 12:
            raise ValidationError("Месяц должен быть от 01 до 12.")

        # Преобразуем в полную дату: 20YY-MM-01
        now = datetime.now()
        full_year = 2000 + year if year < 100 else year
        expiry = datetime(full_year, month, 1)
        if expiry < datetime(now.year, now.month, 1):
            raise ValidationError("Срок действия карты истёк.")
    except ValueError:
        raise ValidationError("Неверный формат даты.")


def validate_cvv(value):
    """Проверяет, что CVV состоит из 3 или 4 цифр."""
    if not value.isdigit():
        raise ValidationError("CVV должен содержать только цифры.")
    if len(value) not in [3, 4]:
        raise ValidationError("CVV должен содержать 3 или 4 цифры.")
