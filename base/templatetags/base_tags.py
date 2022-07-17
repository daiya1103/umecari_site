from django import template

register = template.Library()

@register.simple_tag
def percentage(a, b):
    if b == 0:
        result = False
    else:
        result = a / b
        result = round(result, 3)
    return result