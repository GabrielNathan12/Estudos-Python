from functools import reduce


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

total = 0

for p in produtos:
    total += p['preco']

print(total)

def funcao_do_reduce(acomulador, produto):
    return acomulador + produto['preco']

total_2 = reduce(funcao_do_reduce, produtos, 0)

print(total_2)


total_3 = reduce(lambda acomulador, produto: acomulador + produto['preco'], produtos, 0)

print(total_3)