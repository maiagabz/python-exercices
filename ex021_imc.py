""" IMC
Nesse programa o usuário informe seu peso e altura, e tem como retorno o seu IMC.
Caso ele não esteja dentro do peso, é mostrado qual o peso mínimo/ que a pessoa deveria ter.
IMC = peso / (altura²)
"""

df = "\033[0m"
vm = "\033[1;31m"
vd = "\033[1;32m"
am = "\033[1;33m"

peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))

imc = peso / (altura**2)
#Coloquei essa diferença de 0.1 apenas para facilitar a leitura para o user
min = round(((18.5 * peso) / imc) + 0.1,1)
max = round(((25 * peso) / imc) - 0.1,1)

print(f'IMC: {imc:.2f}','-'*50,sep='\n')
if(imc < 18.5):
    print(f'{am}ATENÇÃO!{df} Você está abaixo do peso.\nO seu peso deveria estar entre {min}kg e {max}kg.')
elif (imc < 25):
    print(f'{vd}PARABÉNS!{df} Você está dentro do peso.')
elif (imc < 30):
    print(f'{am}ATENÇÃO!{df} Você está com sobrepeso.\nO seu peso deveria estar entre {min}kg e {max}kg.')
elif (imc < 35):
    print(f'{vm}ALERTA!{df} Você está com obesidade grau 1.\nO seu peso deveria estar entre {min}kg e {max}kg.')
elif (imc < 40):
    print(f'{vm}ALERTA!{df} Você está com obesidade grau 2.\nO seu peso deveria estar entre {min}kg e {max}kg.')
else:
    print(f'{vm}ALERTA!{df} Você está com obesidade grau 3.\nO seu peso deveria estar entre {min}kg e {max}kg.')