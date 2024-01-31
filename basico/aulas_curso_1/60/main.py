# CPF = 385.622.550-17

# https://www.4devs.com.br/gerador_de_cpf
#import re
import random

cpf = ''

for i in range(9):
    cpf += str(random.randint(0,9))
#cpf = '385.622.550-17'.replace('.','').replace(' ','').replace('-','')

#cpf = re.sub(r'[^0-9]','','385.622.550-17')
print(cpf)
nove_digitos = cpf[:9]

cont_regressivo = 10
resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * cont_regressivo
    cont_regressivo -= 1


primeiro_digito = ((resultado * 10) % 11)
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

print(primeiro_digito)

onze_digitos = cpf[:10]
cont_regressivo_num2 = 11

resultado_num_2 = 0

for digito in onze_digitos:
    resultado_num_2 += int(digito) * cont_regressivo_num2
    cont_regressivo_num2 -= 1


segundo_digito = (resultado_num_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print(segundo_digito)

novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'


if cpf == novo_cpf:
    print('Esse CPF é válido')
else:
    print('Esse CPF é inválido')