""" CONTADOR
O usuário informa os valores inicial, final e intervalo, e o programa vai apresentar a contagem, com um timer de 0.5s
"""

from time import sleep
def linha():
    print('-'*45)

def contagem(i,f,p=1):
    linha()
    print(f'CONTAGEM DE {i} A {f} DE {p} EM {p}')
    f = f - 1 if f < 0 else f + 1
    if i > f: p = p * -1
    for a in range(i,f,p):
        print(a,end=' ')
        sleep(0.5)
    print('FIM!')
    linha()

ini = int(input(f'{"Início:":8}'))
fim = int(input(f'{"Fim:":8}'))
passo = int(input(f'{"Passo:":8}'))
contagem(ini,fim,passo)