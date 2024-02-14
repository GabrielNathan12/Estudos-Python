a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}
              #.keys() pegar as chaves
              # .values() pegar os valores
a, b = pessoa.items()

print(a, b)

for chave, valor in pessoa.items():
    print(chave, valor)


dados_pessoa = {
    'idade': 24,
    'altura': 1.50
}

pessoa_completa = {**pessoa, **dados_pessoa,'chave1': 1}

print(pessoa_completa)


def mostro_arg_nomeados(*args, **kwargs):
    print(kwargs)


mostro_arg_nomeados(nome='Joana', qlq = 11)
mostro_arg_nomeados(**pessoa_completa)