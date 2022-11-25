""" PROGRESSÃO ARITIMÉTICA (10 TERMOS)
O usuário informa 2 valores.
O 1º valor corresponde ao primeiro termo da PA.
O 2º valor corresponde à razão, ou seja, ao valor que será somado a cada termo.
"""

print('PROGRESSÃO ARITIMÉTICA (10 TERMOS)','-'*60,sep='\n')
termo = int(input('Valor inicial: '))
razao = int(input('Razão: '))

#limitando a PA à 10 termos
fim = termo + (10 * razao)
print('-'*60)
for c in range(termo,fim,razao):
    print(c,end=' → ')
print('FIM')