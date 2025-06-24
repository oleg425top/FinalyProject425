import re
from transliterate import translit

def slug_generator(title):
    # Транслитерация русского текста в английский
    transliterated_title = translit(title, 'ru', reversed=True)

    # Замена пробелов и недопустимых символов на дефисы
    slug = re.sub(r'[-\s]+', '-', transliterated_title)

    # Удаление любых оставшихся недопустимых символов
    slug = re.sub(r'[^\w\-]', '', slug)

    # Приведение к нижнему регистру
    slug = slug.lower()

    return slug
