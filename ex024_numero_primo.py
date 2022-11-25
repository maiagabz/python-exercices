""" NÚMEROS PRIMOS
São aqueles que são divisíveis por 1 e por ele mesmo, apenas.
O programa irá mostrar todas as tentativas de divisão do número, de 1 até ele mesmo, e destacar em verde as divisões que não deixam resto.
No final o programa irá mostrar quantas divisões foram feitas e informar se o número é primo ou não.
"""

df = "\033[0m"
vd = "\033[1;32m"
vm = "\033[1;31m"

n = int(input('Informe um número: '))
print('-'*150)

c = 0
for i in range(1,n+1):
    #verifica se o numero é dividido sem deixar resto
    div = n % i == 0
    #se foi dividido mostra em verde
    print(f'{vd if div else df}{i}{df}',end=' ')
    #conta quantas vezes foi dividido
    if div: c +=1 

#printa o resultado final
print('','-'*150,f'O número {n} foi divido {c}x sem deixar resto.',sep='\n')
if(c == 2):
    print(f'Sendo assim, {n} {vd}É PRIMO{df}.')
else:
    print(f'Sendo assim, {n} {vm}NÃO É PRIMO{df}.')