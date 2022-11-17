""" DISSECANDO VARIÁVEL
Esse programa vai pegar o input do usuário e retornar informações básicas sobre ele
"""

df = "\033[0m"
vd = "\033[0;32m"

#Essa função vai padronizar o output como uma tabela
def montaLinha(text, value):
    print(f'{text:15}|{vd if value else df}{str(value):>10}{df}')

def separador():
    print('-'*30)
while True:
    #Quando existe espaço (mesmo entre as palavras), ele não considera como alfanumero e nem alfa
    texto = input('Digite algo ou "sair" para finalizar: ').replace(' ','')

    if texto.lower() == "sair":
        break
    else:
        separador()
        print('Tipo primitivo:', texto.__class__)
        separador()
        
        montaLinha('NUMERICO',  texto.isnumeric())
        montaLinha('DIGITO',    texto.isdigit())
        montaLinha('DECIMAL',   texto.isdecimal())
        separador()
        montaLinha('ALFA',         texto.isalpha())
        montaLinha('ALFANUMERICO', texto.isalnum())
        montaLinha('TITULO',       texto.istitle())
        montaLinha('UPPER',        texto.isupper())
        montaLinha('LOWER',        texto.islower())
        separador()