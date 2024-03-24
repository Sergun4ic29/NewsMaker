from django import template
import re

register = template.Library()

BAD_WORDS = [
    'земельный'
]

@register.filter()
def sort_by(queryset, order):
    return queryset.order_by(order)

@register.filter()
def censor(value):
    for word in BAD_WORDS:
        replace = "".join(['*'] * (len(word)-1))
        value = re.sub(word[1:], replace, value)
    return value




