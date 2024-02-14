pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Nathan',
    'idade': 23,
    'altura': 1.70,
    'casado' : False
}

# retornar a qtd de chaves
print(len(pessoa))

# Retornar as chaves
print(list(pessoa.keys()))
# Retornar os valores
print(list(pessoa.values()))
# retorna uma lista de tupla com a chave e valores
print(list(pessoa.items()))
#Define uma chave padrão
pessoa.setdefault('endereco', None)
print(list(pessoa.items()))
# Se fazer a atribuição de = os 2 discionarios são afetados com a função copy() apenas o que vc quer editar e alterado
pessoa2 = pessoa.copy()

pessoa2['endereco'] = 'Rua tal'

print(pessoa)
print(pessoa2)
# se tiver uma chave que é uma chave mutavel como lista apenas com o copy 
# os 2 discionarios ainda estarao apontado para o mesmo endereco na memoria
# para fazer que eles não seja apontados para a mesmo endereco usa-se o depcopy do modula Python