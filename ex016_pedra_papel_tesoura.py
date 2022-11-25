""" PEDRA, PAPEL, TESOURA
Utiliza a função choice da biblioteca random para selecionar entre 3 opções:
D - Pedra
P - Papel
T - Tesoura
"""
from random import choice

df = "\033[0m"
az = "\033[1;34m"
vm = "\033[1;31m"
vd = "\033[1;32m"

while True:
    print('PEDRA PAPEL TESOURA')
    #lista as opcoes
    op = {'D':'Pedra','P':'Papel','T':'Tesoura'}
    for a,b in op.items():
        print(f'{a}) {b}')
    print('S) Sair')
    #escolha do usuario
    us = str(input('Sua escolha: ''')).upper()

    #caso o usuario deseje sair
    if us == 'S':
        break
    #caso ele tenha digitado algo fora de D,P,T,S
    elif us not in op:
        print(f'{vm}Opção inválida. Tente novamente.{df}','-'*40,sep='\n')
    else:
        #escolha do computador
        pc = choice(list(op))

        print('-'*40,f'Computador escolheu: {op[pc]}.','-'*40,sep='\n')
        #print diferenciado para cada resultado
        if(us == pc):
            print(f'{az}EMPATE!{df}')
        elif (us == 'D' and pc == 'T') or (us == 'P' and pc == 'D') or (us == 'T' and pc == 'P'):
            print(f'{vd}VOCÊ VENCEU!{df}',end=' ')
        else:
            print(f'{vm}VOCÊ PERDEU!{df}',end=' ')

        if (us == 'D' and pc == 'P') or (pc == 'D' and us == 'P'):
            print('PAPEL COBRE PEDRA.')
        elif (us == 'D' and pc == 'T') or (pc == 'D' and us == 'T'):
            print('PEDRA QUEBRA TESOURA.')
        elif (us == 'P' and pc == 'T') or (pc == 'P' and us == 'T'):
            print('TESOURA CORTA PAPEL.')
        print('-'*40)