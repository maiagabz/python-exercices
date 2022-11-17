""" TABELA DE CONVERSÃO DE TEMPERATURAS

O usuário vai informar um valor e uma temperatura inicial, tendo as opções:
1. Celsius (°C)
2. Fahrenheit (°F)
3. Kelvin (°K)

E o programa irá exibir os valores convertidos em formato de tabela
"""

az = "\033[1;34m"
df = "\033[0m"
vm = "\033[1;31m"

def separador():
    print('-'*35)

while True:
    try:
        print(f'''{az}OPÇÕES DE TEMPERATURA{df}
        1. Celsius (°C)
        2. Fahrenheit (°F)
        3. Kelvin (°K)
        ** 99 para sair''')

        separador()
        m1 = int(input('Opção base: '))
        if m1 == 99:
            break
        if m1 not in range(1,4):
            print(f'{vm}Selecione uma opção válida.{df}') 
        else:
            v1 = int(input('Temperatura: '))
            separador()
            print(f'{"°C":^10}|{"°F":^10}|{"°K":^10}|')
            match m1:
                case 1:  
                    print(f'{az}{v1:^10}{df}',end='|')
                    print(format((v1 * 1.8) + 32,'^10.2f'),end='|')
                    print(format(v1 + 273.15,'^10.2f'),end='|')
                case 2:
                    print(format((v1 -32) / 1.8,'^10.2f'),end='|')
                    print(f'{az}{v1:^10}{df}',end='|')
                    print(format(((v1 -32) / 1.8) + 273.15,'^10.2f'),end='|')
                case 3:
                    print(format(v1 - 273.15,'^10.2f'),end='|')
                    print(format(((v1 - 273.15) * 1.8) + 32,'^10.2f'),end='|')
                    print(f'{az}{v1:^10}{df}',end='|')
            print()
            separador()
    except ValueError:
        print(f'{vm}Valor inválido informado!{df}')