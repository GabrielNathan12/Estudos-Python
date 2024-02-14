





def create_function(func):
    def internal(*args, **kwargs):

        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        print('Hellow')
        return result
    return internal

@create_function
def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma String')


invertida = inverte_string('123')
print(invertida)