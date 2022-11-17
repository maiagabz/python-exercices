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
def montaLinha(text, value):
    print(f'{text:25}|{str(value):>14}')

def separador():
    print('-'*40)

while True:
    try:
        num = int(input('Informe um número (999 para sair): '))

        if num == 999:
            break
        else:
            separador()
            montaLinha('ANTECESSOR', num-1)
            montaLinha('SUCESSOR', num+1)
            montaLinha('DOBRO', num*2)
            montaLinha('METADE', f'{num/2:.2f}')
            montaLinha('ELEVADO AO QUADRADO', num**(2))
            montaLinha('RAIZ QUADRADA', f'{num**(1/2):.2f}')
    except ValueError:
        print('Valor deve ser um número!')