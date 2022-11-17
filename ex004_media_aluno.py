""" MÉDIA ALUNO
Nesse programa o usuário informa:
1. A média que ele precisa para ser aprovado
2. As notas dos trabalhos (se houver), separadas por espaço
3. As notas das provas (se houver), separadas por espaço
Com isso o programa irá apresentar a média final e a situação do aluno
"""
med_passar = int(input('Qual a média para passar? '))
trab = list(map(float, input('Informe as notas dos trabalhos separados por espaço: ').split()))
prov = list(map(float, input('Informe as notas das provas separadas por espaço: ').split()))

#MEDIA DOS TRABALHOS
soma_trab = 0
cont_trab = 0
for nota in trab:
    soma_trab += nota
    cont_trab += 1
media_trab = soma_trab / cont_trab

#MEDIA DAS PROVAS
soma_prov = 0
cont_prov = 0
for nota in prov:
    soma_prov += nota
    cont_prov += 1
media_prov = soma_prov / cont_prov

#CORES NO OUTPUT
df = "\033[0m"
vm = "\033[0;31m"
vd = "\033[0;32m"

#MEDIA FINAL
media_final = media_trab + media_prov
print('-'*60)
print(f'''Média final do aluno: {media_final:0.2f}.
Status: {vd + 'aprovado' if media_final >= med_passar else vm +'reprovado'}{df}.''')