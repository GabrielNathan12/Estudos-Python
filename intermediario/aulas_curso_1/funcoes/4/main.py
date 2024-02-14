def escopo():
    def outra_funcao():
        y = 2
        print(x, y)
    x = 1
    outra_funcao()
    print(x)


escopo()