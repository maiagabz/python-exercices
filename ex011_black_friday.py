""" BLACK FRIDAY
Fornece um desconto com base no valor da compra:
- Acima de R$400 = 30% de desconto
- Acima de R$300 = 20% de desconto
- Acima de R$200 = 15% de desconto
- Acima de R$100 = 10% de desconto
- Acima de R$50  =  5% de desconto
"""

df = "\033[0m"
az = "\033[0;34m"
vm = "\033[0;31m"
vd = "\033[0;32m"

total = None
while total == None:
    try:
        preco = float(input('Qual valor da compra? R$'))
        desc = 0
        #30% desconto
        if preco >= 400:
            desc = 30
        #20% desconto
        elif preco >= 300:
            desc = 20
        #15% desconto
        elif preco >= 200:
            desc = 15
        #10% desconto
        elif preco >= 100:
            desc = 10
        #5% desconto
        elif preco >= 50:
            desc = 5

        total = preco * (1-desc/100)

        print('-'*30)
        if desc >= 5:
            print(f'Compra a partir de: R${50 if preco <100 else 400 if preco >=500 else int(preco - (preco % 100))}')
            print(f'{"Desconto: ":20}{vd}{desc}%{df}')
            print('-'*30)
            print(f'{"Total: ":20}{vd}R${total:,.2f}{df}')
        else:
            print('Compra abaixo de R$50.00.')
            print(f'{az}Não aplicável para desconto.{df}')            

    except ValueError:
        print(f'{vm}Valor deve ser um número!{df}')