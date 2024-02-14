s1 = {1,2,3}
s2 = {2,3,4}
# Eles tem as funcoes proprias se caso nao quizer usar a abreviacao como | para uniar ou & para intersecao
s3 = s1 | s2
# Ou s3 = s1.union(s2)
print(s3)
s4 = s1 & s2
print(s4)

s5 = s1 - s2
print(s5)