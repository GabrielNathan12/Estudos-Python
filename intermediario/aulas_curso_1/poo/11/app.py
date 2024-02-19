from dataclasses import asdict, astuple, dataclass
from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    nome: str = field(
        default='default'
    )
    sobrenome: str = 'default'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Gabriel', 'Nathan')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])
    p1 = Pessoa()
    print(p1)