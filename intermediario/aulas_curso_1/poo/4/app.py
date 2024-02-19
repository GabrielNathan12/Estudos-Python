# toString no Python

class Ponto:
    def __init__(self, x: float, y: float, z='str'):
        self.x = x
        self.y = y
        self.z = z

    # toString
    def __str__(self):
        return f'Ponto = ({self.x}, {self.y})'

    # Desenvolvedor
    def __repr__(self):
        return f' ({self.x!r}, {self.y!r} , {self.z!r})'
    
    # a soma de 2 objetos
    def __add__ (self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y

        return Ponto(novo_x, novo_y)
    
    # Comparação
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y


        return result_self > result_other
    

p1 = Ponto(1.4, 3.8)
p2 = Ponto(2.4, 2.3)
p3 = p1 + p2



print(repr(p1))
print(f'{p1}') # assim ou print comun para chamar o __str__

print(p3)

print(p1 > p2)
print(p2 > p1)
