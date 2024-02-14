def gen1():
    yield 1
    yield 2
    yield 3
    yield 4

def gen2():
    yield from gen1()
    yield 5
    yield 6



g = gen2()

for i in g:
    print(i)
