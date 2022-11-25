""" LANCHONETE
Disponibiliza um menu, onde cada item possui um número correspondende.
Através dos números o usuário informa os items que deseja.
Se ele quiser mais de 1 quantidade de cada item, basta apenas repetir o número.
No final o programa vai mostrar a Nota Fiscal com o total do pedido.
"""
print('--------------- MENU ---------------')
menu = {'Hambúrguer':32.5,'Balde Frango':25,'Batata Frita':9,'Regrigerante':4.2,'Milkshake':7,'Casquinha':2.5,'Sundae':5}
idx_menu = {1:'Hambúrguer',2:'Balde Frango',3:'Batata Frita',4:'Regrigerante',5:'Milkshake',6:'Casquinha',7:'Sundae'}

c = 1
for a,b in menu.items():
    print(f'{c}.{a:15}{b:>18}')
    c += 1
print('-'*60)
items = list(map(int, input('Informe os itens desejados separados por espaço: ').split()))

print('----------- NOTA FISCAL -----------')
total = 0
nf = []
for i in items:
    item = idx_menu[i]
    x_item = items.count(i)
    t_item = x_item * menu[idx_menu[i]]    
    
    #não repete o item no output
    if i not in nf:
        nf.append(i)
        print(f'{idx_menu[i]:15}{x_item}x{t_item:>18}')
        total += t_item 
    
print('-'*60)
serv = str(input('Incluir 10% de serviço? [S/N] ')).strip().upper()
if serv == 'S': total *= 1.10
print(f'Total do pedido: R${total:.2f}')