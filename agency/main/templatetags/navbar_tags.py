from django import template
from ..models import Category
from ..forms import UserLoginForm
from django.contrib.auth.models import Group

register = template.Library()


@register.simple_tag()
def get_news():
    Category.objects.all()


@register.simple_tag()
def filtered_category_sale():
    dict_category = {
        'residential': [],
        'country': [],
        'commercial': [],
    }
    sale_category = Category.objects.filter(type_category='ПРОДАЖА')
    for s_cat in sale_category:
        if s_cat.subtype_category == 0:
            dict_category['residential'].append(s_cat)
        elif s_cat.subtype_category == 1:
            dict_category['country'].append(s_cat)
        else:
            dict_category['commercial'].append(s_cat)
    return dict_category
        


@register.simple_tag()
def filtered_category_rent():
    dict_category = {
        'residential': [],
        'country': [],
        'commercial': [],
    }
    rent_category = Category.objects.filter(type_category='АРЕНДА')
    for s_cat in rent_category:
        if s_cat.subtype_category == 0:
            dict_category['residential'].append(s_cat)
        elif s_cat.subtype_category == 1:
            dict_category['country'].append(s_cat)
        else:
            dict_category['commercial'].append(s_cat)
    return dict_category


@register.simple_tag()
def get_login_form():
    return UserLoginForm()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
