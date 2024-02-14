lista = ['a', 1,1.1, True, [0,1,2], (1,2), {0,1}, {'nome': 'Luiz'}]

dado = []
for item in lista:
    if isinstance(item, set):
        dado.append(item)
        #print(item, isinstance(item, dict))
    if isinstance(item, str):
        print(item.upper())

    if isinstance(item, (int, float)):
        print(item, item * 3)

print(dado)