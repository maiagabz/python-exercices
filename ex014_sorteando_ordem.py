""" SORTEANDO ORDEM
Utilização da bilbioteca random para embaralhar as opções fornecidas pelo usuário
"""

import random

alunos = list(map(str, input('Informe o nome dos alunos separados por espaço: ').split()))
#embaralha os items da lista
random.shuffle(alunos)
print(f'A ordem de apresentação será:')
c = 1
for a in alunos:
    print(f'{c}. {a}')
    c +=1