class MeuError(Exception):
    pass


class OutroError(Exception):
    pass


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('você errou isso')
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo o erro')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota de erro')
    raise exception_ from error