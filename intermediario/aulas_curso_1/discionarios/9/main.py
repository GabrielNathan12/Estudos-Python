produto = {
    'nome': 'Caneta Azul',
    'preco': 2.4,
    'categoria': 'Escritório'
}

        # O que será incluido ou como será incluido ou modificado                                   # Filtro dos valores que serão inseridos
dc = { chave:valor.upper() if isinstance(valor, str) else valor for chave, valor in produto.items() if produto.items() if chave != 'categoria'}

print(dc)


s1 = {i for i in range(10)}
print(s1)