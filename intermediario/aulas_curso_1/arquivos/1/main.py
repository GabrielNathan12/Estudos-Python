import os

caminho_arquivo = 'C:\\Users\\gabri\\Documents\\Github\Estudos-Python\\intermediario\\aulas_curso_1\\arquivos\\1\\'
caminho_arquivo += 'arquivo.txt'

#arquivo = open(caminho_arquivo, 'w')

#arquivo.close()


with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))

    arquivo.seek(0,0)

    print(arquivo.read())
    arquivo.seek(0,0)
    print(arquivo.readline().strip())


    arquivo.seek(0,0)

    for linha in arquivo.readlines():
        print(linha.strip())
    print('Arquivo fechado')

print('-' * 10)
with open(caminho_arquivo, 'r') as arquivo:

    print(arquivo.read())



with open(caminho_arquivo, 'a+', encoding='utf-8') as arquivo:
    arquivo.write('Atençao\n')

    arquivo.writelines(('Linha 5\n', 'Linha 6\n'))
    print(arquivo.read())



#os.unlink(caminho_arquivo)
#os.rename(caminho_arquivo, 'arquivo2.txt')