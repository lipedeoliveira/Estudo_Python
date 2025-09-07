# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
from copy import deepcopy

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista = [4,32,1,34,5,6,7,7]
# lista.sort()
# print(lista)

#No caso de um dicionário, o metódo .sort() não sabe
#ordenar, pois usar < e > como medidor para organizar
#O que inviabiliza quando se há texto

# def ordena(item):
#     return item['nome']
def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista,key=lambda item: item['nome'])
l2 = sorted(lista,key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)