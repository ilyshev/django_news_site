from django import template
from django.db.models import Count

from news.models import Category

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0) # если в рубрике нет новостей, то она не выводится в списке рубрик
    return {'categories': categories}