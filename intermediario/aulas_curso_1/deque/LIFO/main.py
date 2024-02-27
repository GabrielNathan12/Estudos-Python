class Fila:
    def __init__(self):
        self.fila = []

    def adicionar(self, elemento):
        self.fila.append(elemento)

    def remover(self):
        if not self.vazia():
            return self.fila.pop(0)

    def vazia(self):
        return len(self.fila) == 0
    
    def __str__(self):
        print(self.fila)
        return ''

fila = Fila()

# Adicionando elementos na fila
fila.adicionar(10)
fila.adicionar(20)
fila.adicionar(30)
print(fila)
# Removendo elementos da fila
elemento = fila.remover()

print(fila)
########### Ou usando do próprio Python
from queue import Queue

fila = Queue()

# Adicionando elementos na fila
fila.put(10)
fila.put(20)
fila.put(30)

# Removendo elementos da fila
elemento = fila.get()
