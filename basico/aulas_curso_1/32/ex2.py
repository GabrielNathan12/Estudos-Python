try:
    valor = input('Digite um horário: ')

    valor = int(valor)

    if valor  >= 0 and valor <= 11:
        print('Bom dia')
    elif valor >= 12 and valor <= 17:
        print('Boa tarde')
    elif valor >= 18 and valor <= 23:
        print('Boa noite')
    else:
        print('Não conheço esse horário')

except:
    print('O valor digitado não é um inteiro')