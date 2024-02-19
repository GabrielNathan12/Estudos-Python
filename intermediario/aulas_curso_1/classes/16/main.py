class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome

class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome


carro = Carro('Fusca')

fabricante = Fabricante('Volkswagen')
motor = Motor('1.0')

carro.fabricante = fabricante

carro.motor = motor


print(carro.nome, carro.fabricante.nome, carro.motor.nome)

