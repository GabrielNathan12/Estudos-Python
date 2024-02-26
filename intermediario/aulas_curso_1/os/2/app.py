import os
from itertools import count

print(os.path.abspath('.'))

counter = count()

caminho = os.getcwd() + '\\intermediario\\aulas_curso_1'

for root, dirs, files in os.walk(caminho):
    ther_counter = next(counter)
    print(ther_counter, 'Pasta: ', root)

    for dir_ in dirs:
        print('   ', ther_counter, 'Dir: ', dir_)

    for file_ in files:
        print('   ', ther_counter, 'File: ', file_)
