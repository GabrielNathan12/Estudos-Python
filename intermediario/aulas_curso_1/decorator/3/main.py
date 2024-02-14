def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_funcoes(func):
        print('Decorado 1')

        def aninhada(*args, **kwargs):
            print('Parametros do decorador', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        
        return  aninhada
    return fabrica_funcoes



@fabrica_de_decoradores(1,2,3)
def soma(x, y):
    return x + y

multiplica = fabrica_de_decoradores(1,2,3)(lambda x, y: x*y)

print(multiplica(19, 5))

dez_mais_cinco = soma(10,5)

print(dez_mais_cinco)