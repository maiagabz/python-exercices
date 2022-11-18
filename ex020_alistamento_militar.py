""" ALISTAMENTO MILITAR
O programa retorna se o usuário está apto para o alistamento com base no seu ano de nascimento
Uiltização da biblioteca datetime
"""

from datetime import date

ano_nasc = int(input('Informe seu ano de nascimento: '))
print('-'*60)
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'Você tem {idade} anos.')
if(idade < 18):
    print(f'Ainda faltam {18 - idade} ano(s) para o alistamento, que será em {ano_atual + (18 - idade)}.')
elif(idade > 18):
    print(f'Você já passou pelo alistamento em {ano_atual - (idade - 18)}.')
else:
    print('Seu alistamento é esse ano. Parabéns!')