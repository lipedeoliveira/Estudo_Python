""""
f'{coluna=}'

usar um '=' juntamente dentro de um colchetes usando f string, permite ver a variavel e seu valor no momento que for printado

"""

qntd_linhas = 5
qntd_colunas = 5

linha = 1 

while linha<= qntd_linhas:
    coluna = 1
    while coluna<= qntd_colunas:
        print(f'{linha=}   {coluna=}')
        coluna+=1
    linha +=1
print("Acabou")