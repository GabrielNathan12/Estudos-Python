l1 = [1,2,3,4,5,6,7]
l2 = [2,3,4,5] 

lista_soma = []

for i in range(len(l2)):
    lista_soma.append(l1[i] + l2[i])

print(lista_soma)


lista_soma2 = []

for i, _ in enumerate(l2):
    lista_soma2.append(l1[i] + l2[i])

print(lista_soma2)


# Uni as 2 listas em uma 
lista_soma3 = [ x + y for x, y in list(zip(l1, l2))]

print(lista_soma3)