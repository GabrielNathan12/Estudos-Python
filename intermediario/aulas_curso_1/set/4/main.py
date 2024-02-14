letras = set()

while True:
    letra = input('Encontre a letra misteriosa: ')
    letras.add(letra.lower())

    if 'g' in letras:
        print(f'Você acertou a letra = {letra}')
        break

    print(letras)