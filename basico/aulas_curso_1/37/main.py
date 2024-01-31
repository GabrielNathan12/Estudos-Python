nome = 'Gabriel Nathan'

contador = 0
nova_str = ''

while contador < len(nome):
    letra = nome[contador]
    nova_str += f'@{letra}'
    contador += 1

nova_str += '@'
print(nova_str)