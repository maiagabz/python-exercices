""" CODIGO ANSI DAS CORES E FORMATAÇÃO DE TEXTO

Codigo das cores
default = "\033[0m"
preto = "\033[0;30m"
vermelho = "\033[0;31m"
verde = "\033[0;32m"
amarelo = "\033[0;33m"
azul = "\033[0;34m"
roxo = "\033[0;35m"
ciano = "\033[0;36m"
branco = "\033[0;37m"

O número depois do [ determina a formatação:
0 Regular
1 Negrito
3 Itálico
4 Sublinhado
7 Destacado

O programa vai te dar a opção de selecionar uma cor, e então mostrar as opções de formatação possíveis.

"""
default = "\033[0m"
cores = ["preto","vermelho","verde","amarelo","azul","roxo","ciano","branco"]
form = ["regular","negrito","-","itálico","sublinhado","-","-","destacado"]

def separador():
    print('-'*40)

while True:
    try:
        print('''SELECIONE UMA COR:
0 - Preto
1 - Vermelho
2 - Verde
3 - Amarelo
4 - Azul
5 - Roxo
6 - Ciano
7 - Branco
99 - Sair''')
        separador()
        sel = int(input('Sua escolha: '))

        if sel == 99:
            break
        elif sel not in range(0,8):
            print('Número informado não é uma opção.')
            separador()
        else:

            separador()
            for i in range(0,8):
                #Atribui a cor escolhida a cada um dos tipos de formatação
                cor_sel = '\033['+str(i)+';3'+str(sel)+'m'
                nm_cor_sel = cores[sel]
                nm_for_sel = form[i]

                #não existe formatacao com os numeros 2,5 e 6
                if(i != 2 and i != 5 and i != 6):
                    #Faz um output dos tipos de formatação
                    print(f'{cor_sel}Texto {nm_cor_sel} {nm_for_sel}: "\\033[{str(i)};3{str(sel)}m".{default}')
                    separador()

            #BACKGROUND
            bg = '\033[4'+str(sel)+'m'
            print(f'{bg}Cor de fundo {nm_cor_sel}: "\\033[4{str(sel)}m".{default}')
            separador()
    
    except ValueError:
            print('Valor informado precisa ser numérico.')
            separador()