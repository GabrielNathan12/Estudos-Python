class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Gabriel', 'Nathan')

print(p1.nome, p1.sobrenome)