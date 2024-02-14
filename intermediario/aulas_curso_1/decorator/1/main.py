def create_function(func):
    def internal(*args, **kwargs):

        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        return result
    return internal

def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma String')

inverte_string_checando_param = create_function(inverte_string)

invertida = inverte_string_checando_param('123')
print(invertida)