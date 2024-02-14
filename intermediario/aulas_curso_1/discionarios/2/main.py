pessoa = {}
chave = 'nome'

#criar
pessoa[chave] = 'Gabriel'
pessoa['sobrenome'] = 'Nathan'
#Atualizar
pessoa[chave] = 'Luiz'
#Deletar
del pessoa['sobrenome']

print(pessoa)