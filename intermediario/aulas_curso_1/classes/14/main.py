#Agreagação

class CarrinhoDeCompras:
    def __init__(self) -> None:
        self._produtodos = []

    def total(self):
        return sum([p.preco for p in self._produtodos])
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtodos.append(produto)

    def listar_produtos(self):
        for produto in self._produtodos:
            print(produto.nome, produto.preco)
        print()



class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco


carrinho = CarrinhoDeCompras()

p1, p2 = Produto('Café', 14.9), Produto('Arroz', 20)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)

carrinho.listar_produtos()
print(carrinho.total())