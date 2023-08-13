from django import template

register = template.Library()


@register.filter()  #используется в product_list.html
def mediapath(value):
    if value:
        return f'/media/{value}'
    else:
        return ''


@register.simple_tag()  #используется в index.html
def mediapath(value):
    if value:
        return f'/media/{value}'
    else:
        return ''
