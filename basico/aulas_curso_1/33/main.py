condicao = True

while condicao:
    nome = input('Seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Saiu')