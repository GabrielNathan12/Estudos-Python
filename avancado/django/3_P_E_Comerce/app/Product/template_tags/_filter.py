from django.template import Library
from utils import utils

register = Library()

@register.filter(name='formact_price')
def formact_price(val):
    return utils.formact_price(val)

@register.filter(name='cart_total_qtd')
def cart_total_qtd(car):
    return utils.cart_total_qtd(car)

@register.filter(name='cart_totals')
def cart_totals(car):
    return utils.cart_totals(car)