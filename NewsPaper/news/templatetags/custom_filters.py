from django import template
import re
from news.models import Category,PostCategory

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

@register.filter()
def curent_category(new):
    my_category = PostCategory.post.objects.get(pk=new.pk)
    return my_category



