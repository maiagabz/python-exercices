""" SEQUÊNCIA DE FIBONACCI
A soma de 2 elementos define o proximo
"""

a = int(input('1º elemento: '))
b = int(input('2º elemento: '))
termos = int(input('Quantos termos você quer mostrar? '))
print('-'*150)
for i in range(0,termos):
    print(a, end=' → ')
    a,b = b, a+b
print('FIM')