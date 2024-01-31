
try:
    valor = input('Digite um número inteiro: ')
    valor = int(valor)

    if valor % 2 == 0:
        print('O numero é par')
    else:
        print('O numero é impar')  
except:
    print('O valor digitado não é um inteiro')


