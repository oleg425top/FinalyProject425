import re
from transliterate import translit


def slug_generator(title):
    """
        Генерирует slug из заданного заголовка.

        Преобразует русский текст в транслит, заменяет пробелы и недопустимые символы на дефисы,
        удаляет оставшиеся недопустимые символы и приводит строку к нижнему регистру.

        Args:
            title (str): Исходный заголовок для преобразования в slug.

        Returns:
            str: Сгенерированный slug.
        """
    # Транслитерация русского текста в английский
    transliterated_title = translit(title, 'ru', reversed=True)

    # Замена пробелов и недопустимых символов на дефисы
    slug = re.sub(r'[-\s]+', '-', transliterated_title)

    # Удаление любых оставшихся недопустимых символов
    slug = re.sub(r'[^\w\-]', '', slug)

    # Приведение к нижнему регистру
    slug = slug.lower()

    return slug
