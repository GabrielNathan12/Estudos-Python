#x, y, *resto = 1, 2, 3, 4

#print(x, y, resto)

def soma(*args):
    soma = 0
    
    for i in args:
        soma  += i
    return soma

num = 1,3,4,5,3,1,4,6,78,9,0

print(soma(*num))