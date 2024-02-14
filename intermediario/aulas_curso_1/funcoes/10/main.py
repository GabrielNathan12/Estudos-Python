def criar_multiplicar(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    
    return multiplicar


duplicar = criar_multiplicar(2)
triplicar = criar_multiplicar(3)
quadrplicar = criar_multiplicar(4)

print(duplicar(3))
print(triplicar(8))
print(quadrplicar(15))


