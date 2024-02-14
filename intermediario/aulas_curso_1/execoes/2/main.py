

try:
    a = 10
    b = 1
    
    #print(b[1])
    print('A'[100])
    c = a / b
    print('B')
    
    print(c)

except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e.__class__.__name__)
except (TypeError, IndexError) as erro:
    print(erro)
    print(erro.__class__.__name__)
except Exception:
    print('Erro desconhecido')

#print('Não será executado daqui para baixo')