p1 = {
    'nome' : 'Miranda',
    'sobrenome': 'Henrique'
}

# apaga a chave e o valor
# mas ainda consegue pegar o valor da chave apagada
nome = p1.pop('nome')
print(nome)

print(p1)

# Atualizar
# se a chave nao existir, se a chave existir ele atualizar o valor

p1.update(nome='Gabriel', sobrenome='Nathan', idade=23)
print(p1)