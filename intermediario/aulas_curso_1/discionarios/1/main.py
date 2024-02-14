pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Nathan',
    'idade': 23,
    'altura': 1.70,
    'casado' : False,
    'enderecos': [
        {'rua x': 'Em tal rua', 'numero': 123},
        {'rua y': 'Perto de lugar tal','numero': 456}
    ]
}


#print(pessoa, type(pessoa))
#print(pessoa['enderecos'])


for chave in pessoa:
    print(chave , pessoa[chave])