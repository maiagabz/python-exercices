""" ANALISANDO TRIÂNGULO
1. O programa analisa se um triângulo pode ser formado a partir dos valores de 3 segmentos informados pelo usuário
2. Se um triângulo pode ser formado, o programa mostra qual o tipo, seguindo as regras:
- Escaleno: todos os lados possuem medidas diferentes; 
- Isósceles: existem dois lados que possuem mesma medida; 
- Equilátero: todos os lados são congruentes.
"""

df = "\033[0m"
vm = "\033[0;31m"

#a soma das medidas de dois lados é sempre maior que a medida do terceiro
segmentos = list(map(int,input('Informe 3 segmentos separados por espaço: ').split()))
l1,l2,l3 = segmentos
triangulo = (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1)
if(triangulo):
    print('Os seguimentos acima podem formar um triângulo ',end='')
    if(l1 == l2 == l3):
        print('EQUILÁTERO!')
    elif(l1 != l2 != l3):
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print(f'{vm}Os seguimentos acima não podem formar um triângulo!{df}')