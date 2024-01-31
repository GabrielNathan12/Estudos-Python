qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    #print(linha)

    colunas = 1

    while colunas <= qtd_colunas:
        print(linha,colunas)
        colunas += 1
    
    linha += 1

print('Acabou o while')