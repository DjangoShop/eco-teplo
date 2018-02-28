from django import template

# Реализация фильтра 
register = template.Library()
@register.filter
def increase_perc_filter(price):
    pre_precent = price/100 * 13
    return price + pre_precent