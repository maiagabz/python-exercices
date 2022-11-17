""" TABELA DE CONVERSÃO DE MEDIDAS

O usuário vai informar um valor, e o programa irá exibir os valores convertidos em formato de tabela:

- Decimal
- Binário
- Hexadecimal
- Octal
"""


az = "\033[1;34m"
df = "\033[0m"
vm = "\033[1;31m"

def separador():
    print('-'*45)

while True:
    try:
        v1 = int(input('Informe um valor ou 99 para sair: '))
        if v1 == 99:
            break
        else:
            separador()
            print(f'{"DEC":^10}|{"BIN":^10}|{"HEX":^10}|{"OCT":^10}|')
            print(f'{az}{v1:^10}{df}',end='|')
            print(f'{bin(v1)[2:]:^10}',end='|')
            print(f'{hex(v1)[2:]:^10}',end='|')
            print(f'{oct(v1)[2:]:^10}',end='|')
            print()
            separador()
    except ValueError:
        print(f'{vm}Valor inválido informado!{df}')