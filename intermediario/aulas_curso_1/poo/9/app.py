import enum


#Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = 2
    ACIMA = 3
    ABAIXO = 4

def mover(direcoes: Direcoes):
    if not isinstance(direcoes, Direcoes):
        raise ValueError('Direção não encontrada')
    
    print(f'Movendo para {direcoes.name}')


mover(Direcoes.DIREITA)
mover(Direcoes.ESQUERDA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)

