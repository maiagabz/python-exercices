""" PALÍNDROMO
Um palíndromo consiste numa palavra que fica igual quando está de trás para frente.
"""

df = "\033[0m"
vm = "\033[0;31m"
vd = "\033[0;32m"

a = str(input('Digite uma frase: ')).strip().upper()
b = a.replace(' ','')
#inverte a b
pali = b[::-1]

print('-'*60)
print(f'O inverso de "{a}" é {pali}.')
if(b == pali):
    print(f'{vd}A frase digitada é um palíndromo!{df}')
else:
    print(f'{vm}A frase digitada não é um palíndromo.{df}')