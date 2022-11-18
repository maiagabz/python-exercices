""" BRINCANDO COM NÚMEROS
Esse programa vai pegar o número informado pelo usuário e retornar:
- Antecessor
- Sucessor
- Dobro
- Metade
- Elevado ao quadrado
- Raiz quadrada
"""

#Essa função vai padronizar o output como uma tabela
import math

def montaLinha(text, value):
    print(f'{text:25}|{str(value):>14}')

def separador():
    print('-'*40)

num = None
while num == None:
    try:
        num = int(input('Informe um número: '))

        if num == 999:
            break
        else:
            separador()
            montaLinha('ANTECESSOR', num-1)
            montaLinha('SUCESSOR', num+1)
            montaLinha('DOBRO', num*2)
            montaLinha('METADE', f'{num/2:.2f}')
            #math.pow() = calcula potência
            montaLinha('ELEVADO AO QUADRADO', math.pow(num, 2))
            #math.sqrt() = calcula raiz quadrada
            montaLinha('RAIZ QUADRADA', f'{math.sqrt(num):.2f}')
    except ValueError:
        print('Valor deve ser um número!')