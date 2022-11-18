""" CÁLCULO DE SENO, COSSENO, TANGENTE
Utilização da bilbioteca math com as funções:
- radians
- sin
- cos
- tan
"""

df = "\033[0m"
vm = "\033[0;31m"

from math import radians, sin, cos, tan

a = None
while a == None:
    try:
        a = float(input('Informe o ângulo desejado: '))
        print('-'*30)
        print(f"{'SENO:':10}{sin(radians(a)):.2f}")
        print(f"{'COSSENO:':10}{cos(radians(a)):.2f}")
        print(f"{'TANGENTE:':10}",end='')
        #não existe tangente de 90º
        if a == 90:
            print('∄')
        else:
            print(f"{tan(radians(a)):.2f}")
    except ValueError:
        print(f'{vm}Valor deve ser um número!{df}')