""" TABELA DE CONVERSÃO DE MEDIDAS

O usuário vai informar um valor e uma medida inicial, tendo as opções:
1. Quilômetro (km)
2. Metro (m)
3. Centímetro (cm)
4. Milímetro (mm)

E o programa irá exibir os valores convertidos em formato de tabela
"""

az = "\033[1;34m"
df = "\033[0m"
vm = "\033[1;31m"

def separador():
    print('-'*65)

while True:
    try:
        print(f'''{az}OPÇÕES DE MEDIDA{df}
        1. Quilômetro (km)
        2. Metro (m)
        3. Centímetro (cm)
        4. Milímetro (mm)
        ** 99 para sair''')

        separador()
        m1 = int(input('Medida inicial: '))
        if m1 == 99:
            break
        if m1 not in range(1,5):
            print(f'{vm}Selecione uma opção válida.{df}') 
        else:
            v1 = float(input('Valor inicial: '))
            separador()
            print(f'{"KM":^15}|{"M":^15}|{"CM":^15}|{"MM":^15}|')
            match m1:
                case 1:  
                    print(f'{az}{v1:^15}{df}',end='|')
                    print(f'{v1 * 1000:^15}',end='|')
                    print(f'{v1 * 100000:^15}',end='|')
                    print(f'{v1 * 1000000:^15}',end='|')
                case 2:
                    print(f'{v1 / 1000:^15}',end='|')
                    print(f'{az}{v1:^15}{df}',end='|')
                    print(f'{v1 * 100:^15}',end='|')
                    print(f'{v1 * 1000:^15}',end='|')
                case 3:
                    print(f'{v1 / 100000:^15}',end='|')
                    print(f'{v1 / 100:^15}',end='|')
                    print(f'{az}{v1:^15}{df}',end='|')
                    print(f'{v1 * 10:^15}',end='|')
                case 4:
                    print(f'{v1 / 1000000:^15}',end='|')
                    print(f'{v1 / 1000:^15}',end='|')
                    print(f'{v1 / 10:^15}',end='|')
                    print(f'{az}{v1:^15}{df}',end='|')
            print()
            separador()
    except ValueError:
        print(f'{vm}Valor inválido informado!{df}')