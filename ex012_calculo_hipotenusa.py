""" CÁLCULO DE HIPOTENUSA 
a² + b² = c²
"""

df = "\033[0m"
vm = "\033[0;31m"

c = None
while c == None:
    try:
        a = float(input('Cateto oposto: '))
        b = float(input('Cateto adjacente: '))
        c = ((a**2) + (b**2)) ** (1/2)
        print(f'A hipotenusa vai medir {c:.2f}')
    except ValueError:
        print(f'{vm}Valor deve ser um número!{df}')