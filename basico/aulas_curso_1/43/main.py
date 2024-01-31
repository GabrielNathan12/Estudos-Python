import os

palavra_secreta = 'criptografia'
letras_acertadas = ''
num_tentativas = 0

while True:
    letra_usuario = input('Digite uma letra: ')
    num_tentativas += 1
    
    if len(letra_usuario) > 1:
        print('Digite apenas uma letra: ')
        continue

    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra secreta: ' , palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ ACERTOU !!!')
        print('A palavra secreta: ',palavra_formada)
        print('Número de tentativas: ' , num_tentativas)
        letras_acertadas = ''
        num_tentativas = 0