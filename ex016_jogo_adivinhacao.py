""" JOGO ADIVINHAÇÃO
Utilização da bilbioteca random para sortear um número aleatório entre 0 e 10
"""

from random import randint

def separador():
    print('-'*60)

while True:
    print('Vou pensar em um número de 0 a 10, tente adivinhar...')
    num = int(input('Em que número eu pensei? '))
    separador()
    ran = randint(0,10)
    if num not in range(0,11):
        print('Número precisa estar entre 0 e 10!')
    elif(num == ran):
        print('ACERTOU! Grandes mentes pensam iguais :)')
    else:
        print(f'ERROU! Eu pensei no número {ran} e não no {num}!')
    separador()