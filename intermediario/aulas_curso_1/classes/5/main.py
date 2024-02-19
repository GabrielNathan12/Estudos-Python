class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade



    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    



p1 = Pessoa('Gabriel', 23)
p2 = Pessoa('Nathan', 24)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
