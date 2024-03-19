import string
from random import SystemRandom
from django.utils.text import slugify

def random_letters(size=5) ->str :
    return ''.join(SystemRandom().choices(string.ascii_letters + string.digits, k=size))


def new_slugify(text)->str:
    return slugify(text) + '-' + random_letters()