""" FATORIAL
n! = n . (n – 1). (n – 2)
"""

n = int(input('Informe um número: '))
print('-'*150)

print(f'Calculando {n}! =',end=' ')
fat = 1
for i in range(n,0,-1):
    print(i,'=' if i == 1 else 'x',end=' ')
    fat *= i  
print(fat)