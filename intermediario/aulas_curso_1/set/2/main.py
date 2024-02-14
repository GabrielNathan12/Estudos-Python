s1 = set()

#adcionar dados no set
s1.add('Luiz')
s1.add('Gabriel')
s1.add(1)
print(s1)

# atualizar

s1.update(('Olá Mundo', 1,2,3,4,5))

print(s1)

#Deletar

s1.discard(1)
print(s1)