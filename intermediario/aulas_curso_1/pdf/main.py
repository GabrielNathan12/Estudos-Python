from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


PASTA_RAIZ =  Path(__file__).parent
PASTA_ORI = PASTA_RAIZ / 'pdf_original'
NOVA_PASTA = PASTA_RAIZ / 'arquivo_novo'

RELATORIO_BACEN = PASTA_ORI / 'R20230210.pdf'

NOVA_PASTA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

#print(len(reader.pages))

#for page in reader.pages:
    #print(page)
    #print()

page0 = reader.pages[0]

imagem0 = page0.images[10]
#print(page0.extract_text())
#print(page0.images[0])
# Ler
with open(NOVA_PASTA/ imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)



writer = PdfWriter()
writer.add_page(page0)
# Escrever


with open(NOVA_PASTA / 'page0.pdf', 'wb') as fp:
    #for page in reader.pages:
        #writer.add_page(page)
    writer.write(fp)
"""
Separar cada página em um arq novo
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NOVA_PASTA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore
"""
