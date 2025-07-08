from django import template

register = template.Library()


@register.filter()
def brand_media(val):
    if val:
        return fr'/media/{val}'
    return '/static/no_image.jpg'


@register.filter()
def tool_media(val):
    if val:
        return f'/media/{val}'
    return '/static/no_image.jpg'


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context['request'].GET.copy()
    for key, value in kwargs.items():
        query[key] = value
    return query.urlencode()
