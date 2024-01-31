frase = 'É apenas , uma frase'

lista_palavras = frase.split()

for i, frase in enumerate(lista_palavras):
    # Remove os espaços da string strip()
    lista_palavras[i] = lista_palavras[i].strip()

    #print(lista_palavras[i].strip())

frases = '-'.join('abcd')
print(lista_palavras)
print(frases)