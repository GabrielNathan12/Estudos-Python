from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'arq.csv'


with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for l in leitor:
        print(l)

print()
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for l in leitor:
        print(l)