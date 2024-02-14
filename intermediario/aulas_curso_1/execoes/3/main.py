try:
    print(1)
    #9/0
except:
    print('Ocorreu um erro')
else:
    print('Não deu erro')
finally: # Sempre será executado mesmo se ocorrer uma exeção
    print('Finally')

# try pode ser executado com quantos except quiser ou apenas um finally ou os 2