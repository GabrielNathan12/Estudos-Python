import os

lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    
    elif opcao == 'a':
        indice_str = input('Escolha um índice para remover: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Esse índice não existe na lista, tente novamente')
    
    elif opcao == 'l':
        os.system('cls')

        if len(lista) ==0:
            print('Não há nada na lista')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Não conheço essa opção')