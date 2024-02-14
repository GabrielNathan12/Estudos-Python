def adiciona_clientes(nome, lista=None):

    if lista == None:
        lista = []
    lista.append(nome)

    return lista


cliente = adiciona_clientes('Gabriel')
adiciona_clientes('Joana', cliente)
print(cliente)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
print(cliente2)