""" SEPARANDO DÍGITO
Destrincha um numeral, informando a unidade, dezena, centena e milhar
"""

num = int(input('Informe um número de 0 a 9000: '))
#// = pega a parte inteira da divisao
#% = pega o restante (parte decimal)
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f"""------------
{'Unidade':7}: {uni}
{'Dezena':7}: {dez}
{'Centeza':7}: {cen}
{'Milhar':7}: {mil}
""")