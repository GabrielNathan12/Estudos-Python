from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


Carta = namedtuple(
     'Carta', ['valor', 'naipe'],
     defaults=['VALOR', 'NAIPE']
)

as_espadas = Carta('A')

print(as_espadas._asdict())
print(as_espadas)
print(as_espadas[0])
print(as_espadas.valor)
print(as_espadas[1])
print(as_espadas.naipe)

print()
print(as_espadas._fields)
print(as_espadas._field_defaults)


for valor in as_espadas:
    print(valor)