from collections.abc import Callable
from threading import Thread
from time import sleep
from threading import Lock

class MyThread(Thread):
    def __init__(self,texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MyThread('T: 1', 10)
t1.start()
t2 = MyThread('T: 2', 2)
t2.start()
t3 = MyThread('T: 3', 5)
t3.start()

for i in range(20):
    print(i)
    sleep(1)

def vai_demorar(tempo, texto):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demorar, args=(5,'T: Função'))
t.start()

while t.is_alive():
    print('Espera a função')
    sleep(2)


class Ingressos:
    def __init__(self, estoque) -> None:
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Ingressos insuficientes')
            self.lock.release()
            return
        sleep(1)
        self.estoque -= quantidade       
        print(f'Ainda possuimos ingressos: {self.estoque}')
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    
    for i in range(1,20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)