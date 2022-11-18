""" ANO BISSEXTO
Para o ano ser bissexto ele precisa ser divisível por quatro e não pode ser divisível por 100
"""
ano = int(input('Digite um ano: '))
bis = (ano % 4 == 0) and (ano % 100 != 0)
print(ano,'é' if bis else 'não é','um ano bissexto')