def criar_saudacao(saudacao):
    
    def saudar(nome):
        return f'{saudacao}, {nome}'

    return saudar

s1 = criar_saudacao('Boa noite')
s2 = criar_saudacao('Boa tarde')


for i in ['Gabriel', 'Nathan', 'Pedro']:
    print(s1(i))
    print(s2(i))

