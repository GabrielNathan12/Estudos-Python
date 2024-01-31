lista = ['Maria', 'Helena', 'Luiz']
#Pega o primeiro elemento e iguinora o resto
nome1, *_ = lista

_, nome2 , *_ = lista

print(nome1)

print(nome2)