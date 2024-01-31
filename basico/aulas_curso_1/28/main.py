num_str = input('Digite um número ')

try:
    num_str = float(num_str)    
    print(f'Dobro do número é {num_str * 2}')
except:
    print('Não é um número')
