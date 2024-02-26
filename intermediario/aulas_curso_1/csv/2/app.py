import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent /'aulacsv.csv'

lista_clientes = [
    {'Nome': 'Gabriel Nathan', 'Idade': 24},
    {'Nome': 'Maria Joaquina', 'Idade': 21}
]

with open(CAMINHO_CSV, 'w') as arquivo:
    colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo) #DictWriter para mandar o discionario inteiro
    escritor.writerow(colunas)

    for cliente in lista_clientes:
        escritor.writerow(cliente.values())