""" CAIXA ELETRÔNICO
O usuário informa o valor do saque, e o programa calcula quantas notas de cada cédula serão necessárias.
"""

valor = float(input('Valor do saque: R$'))
total = valor
#cedula de maior valor
ced = 100
totalced = 0
print('-'*40)
print('Você irá receber: ')
while True:
    #se o valor do saque atual for maior que da celula
    if total >= ced:
        #tira quantas cedulas desse valor forem possiveis
        total -= ced
        #contabiliza as cedulas
        totalced += 1
    #se o valor que sobrou estiver menor que o valor da cedula
    else:
        if(totalced > 0): print(f'{totalced:2} notas de R${ced}')
        #muda a cedula para a proxima
        match ced:
            case 100:
                ced = 50
            case 50:
                ced = 20
            case 20:
                ced = 10
            case 10:
                ced = 5
            case 5:
                ced = 2
            case 2:
                ced = 1
        #zera o total para contabilizar a nova cedula
        totalced = 0
        #se o valor do total ja zerou, encerra
        if total == 0: break
print('-'*40)