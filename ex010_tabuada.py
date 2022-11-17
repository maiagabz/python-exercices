num = None
while num == None:
    try:
        num = int(input('Informe um número inteiro para tabuada: '))
        print('-'*15)
        for x in range(1,11):
            print(f'{num} x {x:2} = {num*x}')
        print('-'*15)
    except ValueError:
        print('Valor deve ser um número inteiro!')