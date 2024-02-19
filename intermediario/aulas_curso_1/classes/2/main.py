class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')

fusca.acelerar()