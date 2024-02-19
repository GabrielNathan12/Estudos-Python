import json

CAMINHO_ARQ = 'arquivo.json'

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Gabriel', 24)
p2 = Pessoa('Nathan', 30)


bd = [vars(p1), vars(p2)]


with open(CAMINHO_ARQ, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)


with open(CAMINHO_ARQ, 'r') as arquivo:
    dados = json.load(arquivo)

    for pessoa in dados:
        print(pessoa)