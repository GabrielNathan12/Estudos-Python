

try:
    a = 10
    b = 1
    
    print(b[1])
    print('A')
    c = a / b
    print('B')
    
    print(c)

except ZeroDivisionError:
    print('Divisão por 0, não é possível')
except NameError:
    print('b não está definido')
except (TypeError, IndexError):
    print('Erro desconhecido')
except Exception:
    print('Erro desconhecido')

#print('Não será executado daqui para baixo')