# Composição

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for e in self.enderecos:
            print(e.nome, e.rua)

    def __del__(self):
        print('Apagando', self.nome)

class Endereco:
    def __init__(self, nome, rua) -> None:
        self.nome = nome
        self.rua = rua
    
    def __del__(self):
        print('Apagando', self.nome, self.rua)
    


cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Av X', 54)
cliente1.inserir_enderecos('Av y', 67)

#del cliente1
cliente1.listar_enderecos()