lista = ['Maria', 'Helena', 'Luiz']
lista.append('Gabriel')


for i, nome in enumerate(lista):
    print(i, nome)


for i in enumerate(lista):
    indice, nome = i
    print(indice, nome)


