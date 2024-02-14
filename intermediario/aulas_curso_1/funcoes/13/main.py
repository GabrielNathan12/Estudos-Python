def generator(n=0):
    yield 1 #Pausa a execução da função
    print('Proximo valor')
    yield 2
    print('Proximo valor')
    yield 3
    print('Acabou')


def generador_2(n=0, maximo=10):
    while True:
        yield n 
        n += 1

        if n >= maximo:
            return 
        
gen = generator(n=0)
#print(next(gen))
#print(next(gen))
#print(next(gen))


for n in gen:
    print(n)


gen2 = generador_2(maximo=10000)

for n in gen2:
    print(n)