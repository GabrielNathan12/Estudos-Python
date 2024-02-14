def multiplicacao(*args):
    resultado = 1

    for i in args:
        resultado *= i

    return resultado

def num_par_impar(num):

    if num  % 2 == 0:
        return f'{num} é par'

    return f'{num} é ímpar' 


print(multiplicacao(1,4,5,6,7,65,3))
print(multiplicacao(6,8,54,5,34,43,3))

print(num_par_impar(4))
print(num_par_impar(7))
