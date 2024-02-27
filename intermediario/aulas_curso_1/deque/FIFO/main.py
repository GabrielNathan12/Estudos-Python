class Pilha:
     def __init__(self):
         self.items = []

     def estaVazia(self):
         return self.items == []

     def adicionar(self, item):
         self.items.append(item)

     def remover(self):
         return self.items.pop()

     def topo(self):
         return self.items[len(self.items)-1]

     def tamanho(self):
         return len(self.items)
     def __str__(self):
        print(self.items)
    
        return ''
     
pilha = Pilha()
pilha.adicionar(10)
pilha.adicionar(20)
pilha.adicionar(30)

print(pilha)
pilha.remover()
print(pilha)