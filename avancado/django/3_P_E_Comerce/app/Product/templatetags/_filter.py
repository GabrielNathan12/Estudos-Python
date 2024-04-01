from django.template import Library
from utils import utils

register = Library()

@register.filter
def formact_price(val):
    return utils.formact_price(val)

@register.filter
def cart_total_qtd(car):
    return utils.cart_total_qtd(car)

@register.filter
def cart_totals(car):
    return utils.cart_totals(car)