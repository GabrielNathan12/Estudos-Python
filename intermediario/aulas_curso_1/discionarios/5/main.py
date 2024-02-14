perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for i in perguntas:
    print('Pergunta', i['Pergunta'])
    print()

    opcaoes = i['Opções']

    for j, opcao in enumerate(opcaoes):
        print(f'{j}-)', opcao)
    print()
    
    escolhas = input('Escolha uma opção: ')
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcaoes)

    if escolhas.isdigit():
        escolha_int = int(escolhas)

    if escolha_int is not None:
       if escolha_int >= 0 and escolha_int < qtd_opcoes:
           if opcaoes[escolha_int] == i['Resposta']:
               acertou = True

    
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errouuuu ❌')
    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'Perguntas')