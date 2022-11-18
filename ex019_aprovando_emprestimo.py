""" APROVANDO EMPRÉSTIMO
O programa analisa a possibilidade de empréstimo com base nos seguintes dados:
- Valor do imóvel
- Salário do comprador
- Anos de financiamento
"""

df = "\033[0m"
vm = "\033[0;31m"
vd = "\033[0;32m"

valor = float(input('Valor do imóvel: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Anos de financiamento: '))
prestacao = valor / anos / 12
#minimo = 30% salario
minimo = salario * 0.3

print('-'*80)
print(f'Para pagar um imóvel de R${valor:,.2f} em {anos} anos, a prestação seria de R${prestacao:,.2f}.')
print(f"O investimento mínimo com base no seu salário é R${minimo:,.2f}.")
if(minimo >= prestacao):
    print(f'{vd}Empréstimo pode ser concedido.{df}')
else:
    print(f'{vm}Empréstimo não pode ser concedido.{df}')