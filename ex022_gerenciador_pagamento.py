""" GERENCIADOR DE PAGAMENTO
Aplica uma determinada regra baseada na forma de pagamento:
1) À vista no dinheiro/cheque: 10% de desconto
2) À vista no cartão: 5% de desconto
3) 2x no cartão: valor normal
4) 3x ou mais ou cartão: 10% de juros
"""

valor = float(input('Valor da compra: R$'))
print('-'*40)
fm_pag = int(input('''FORMAS DE PAGAMENTO
1) À vista no dinheiro/cheque
2) À vista no cartão
3) 2x no cartão
4) 3x ou mais ou cartão
Qual a opção desejada? '''))
print('-'*40)

match fm_pag:
    #opcao 1 = 10% desconto
    case 1:
        print(f'Você ganhou 10% de desconto.\nO total da sua compra ficou R${valor * 0.9:,.2f}.')
    #opcao 2 = 5% desconto
    case 2:
        print(f'Você ganhou 5% de desconto.\nO total da sua compra ficou R${valor * 0.95:,.2f}.')
    #opcao 3 = valor normal
    case 3:
        print(f'Você pagará 2 parcelas de R${valor/2:,.2f}.')
    #opcao 4: 20% de juros
    case 4:
        num_parcelas = int(input('Em quantas parcelas deseja dividir? '))
        valor_total = valor * 1.1
        valor_parcelas = valor_total / num_parcelas
        print(f'''Com 10% de juros, o total da sua compra é R${valor_total:,.2f}.
A compra será parcelada em {num_parcelas}x de R${valor_parcelas:,.2f}.''')
    case _:
        print('Esta opção é inválida.')