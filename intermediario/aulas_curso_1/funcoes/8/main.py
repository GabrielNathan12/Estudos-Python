
def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)


c = executa(saudacao, 'Bom dia', 'Gabriel')

print(c)