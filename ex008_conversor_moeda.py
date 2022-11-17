""" TABELA DE CONVERSÃO DE MOEDAS

O usuário vai informar um valor e uma moeda inicial, tendo as opções:
1. Real (R$)
2. Dolar ($)
3. Euro (€)
4. Libra (£)

E o programa irá exibir os valores convertidos em formato de tabela

#Esse programa utiliza a biblioteca forex-python, que precisa ser instalada:
$ pip install forex-python
"""

from forex_python.converter import CurrencyRates
c = CurrencyRates()

az = "\033[1;34m"
df = "\033[0m"
vm = "\033[1;31m"

def separador():
    print('-'*65)

while True:
    try:
        print(f'''{az}OPÇÕES DE MOEDA{df}
        1. Real  (R$)
        2. Dolar ($)
        3. Euro  (€)
        4. Libra (£)
        ** 99 para sair''')

        separador()
        m1 = int(input('Moeda inicial: '))
        if m1 == 99:
            break
        if m1 not in range(1,5):
            print(f'{vm}Selecione uma opção válida.{df}') 
        else:
            v1 = float(input('Valor inicial: '))
            separador()
            print(f'{"REAL (R$)":^15}|{"DOLAR ($)":^15}|{"EURO (€)":^15}|{"LIBRA (£)":^15}|')
            match m1:
                case 1:  
                    print(f'{az}{v1:^15}{df}',end='|')
                    print(format(c.convert('BRL', 'USD', v1),'^15.2f'),end='|')
                    print(format(c.convert('BRL', 'EUR', v1),'^15.2f'),end='|')
                    print(format(c.convert('BRL', 'GBP', v1),'^15.2f'),end='|')
                case 2:
                    print(format(c.convert('USD', 'BRL', v1),'^15.2f'),end='|')
                    print(f'{az}{v1:^15}{df}',end='|')
                    print(format(c.convert('USD', 'EUR', v1),'^15.2f'),end='|')
                    print(format(c.convert('USD', 'GBP', v1),'^15.2f'),end='|')
                case 3:
                    print(format(c.convert('EUR', 'BRL', v1),'^15.2f'),end='|')
                    print(format(c.convert('EUR', 'USD', v1),'^15.2f'),end='|')
                    print(f'{az}{v1:^15}{df}',end='|')
                    print(format(c.convert('EUR', 'GBP', v1),'^15.2f'),end='|')
                case 4:
                    print(format(c.convert('GBP', 'BRL', v1),'^15.2f'),end='|')
                    print(format(c.convert('GBP', 'USD', v1),'^15.2f'),end='|')
                    print(format(c.convert('GBP', 'EUR', v1),'^15.2f'),end='|')
                    print(f'{az}{v1:^15}{df}',end='|')
            print()
            separador()
    except ValueError:
        print(f'{vm}Valor inválido informado!{df}')