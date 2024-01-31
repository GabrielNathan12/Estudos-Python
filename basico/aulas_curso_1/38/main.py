while True:

    num_1 = input('Digite um número: ')
    num_2 = input('Digite um número: ')
    operarador = input('Digite  o operador (+-/*): ')

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)

        if num_2 == 0 and operarador == '/':
            print('Divisão por 0 não é válida')
            continue

        if operarador == '+':
            print(f'{num_1} + {num_2} = {num_1 + num_2}')
        
        elif operarador == '-':
            print(f'{num_1} - {num_2} = {num_1 - num_2}')
        
        elif operarador == '*':
            print(f'{num_1} * {num_2} = {num_1 * num_2}')
        
        elif operarador == '/':
            print(f'{num_1} / {num_2} = {num_1 / num_2}')
        else:
            print('Tipo de operação não suportada')

    except:
        print('Entre com apenas números')
    sair = input('Encerrar programa ? \n[S]im:  ').lower().startswith('s')
    
    if sair:
        break
