"""
Lista de listas e seus indices

"""

salas = [
    #0....1
    ['Maria','Helena',],#0
    #  0
    ['Elaine',],#1
    
    #0         1       2
    ['Luiz','João','Eduarda',(0,10,20,30,40)],#2
    
]

# Funciona como uma matriz, primeiro se passa a linha, depois o indice do objeto a buscar
# print(salas[2][3])
# Para buscar um item, dentro de uma lista/tupla, se passa mais um jogo de [] junto 
# ao indice do item dentro daquela lista
# print(salas[2][3][2])

for sala in salas:
    print(f'\nSala{sala}')
    for aluno in sala:
        print(aluno)    