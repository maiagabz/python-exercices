""" TABELA DE CONVERSÃO DE MEDIDAS

O usuário vai informar um valor e uma medida inicial, tendo as opções:
1. Tonelada (t)
2. Quilograma (kg)
3. Grama (g)
4. Miligrama (mg)

E o programa irá exibir os valores convertidos em formato de tabela
"""

az = "\033[1;34m"
df = "\033[0m"
vm = "\033[1;31m"

def separador():
    print('-'*85)

while True:
    try:
        print(f'''{az}OPÇÕES DE MEDIDA{df}
        1. Tonelada (t)
        2. Quilograma (kg)
        3. Grama (g)
        4. Miligrama (mg)
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
            print(f'{"T":^20}|{"KG":^20}|{"G":^20}|{"MG":^20}|')
            match m1:
                case 1:  
                    print(f'{az}{v1:^20}{df}',end='|')
                    print(f'{v1 * 1000:^20}',end='|')
                    print(f'{v1 * 1000000:^20}',end='|')
                    print(f'{v1 * 1000000000:^20}',end='|')
                case 2:
                    print(f'{v1 / 1000:^20}',end='|')
                    print(f'{az}{v1:^20}{df}',end='|')
                    print(f'{v1 * 1000:^20}',end='|')
                    print(f'{v1 * 1000000:^20}',end='|')
                case 3:
                    print(f'{v1 / 1000000:^20}',end='|')
                    print(f'{v1 / 1000:^20}',end='|')
                    print(f'{az}{v1:^20}{df}',end='|')
                    print(f'{v1 * 1000:^20}',end='|')
                case 4:
                    print(f'{v1 / 1000000000:^20}',end='|')
                    print(f'{v1 / 1000000:^20}',end='|')
                    print(f'{v1 / 1000:^20}',end='|')
                    print(f'{az}{v1:^20}{df}',end='|')
            print()
            separador()
    except ValueError:
        print(f'{vm}Valor inválido informado!{df}')