"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
import os
os.system('cls')
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],#0
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],#1
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],#2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],#3
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],#4
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],#5
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],#6
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],#7
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],#8
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],#9
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],#10
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],#11
]
lista_verificadora = []
size_row = int(len(lista_de_listas_de_inteiros[0]))
for i in range(len(lista_de_listas_de_inteiros)):
    count = 0
    for c in range(len(lista_de_listas_de_inteiros[i])):
        x = lista_de_listas_de_inteiros[i][c]
        if x in lista_verificadora:
            print(f"Linha::{i} >{x}<")
            break
        elif x not in lista_verificadora and count == 0:
            lista_verificadora.append(x)
        elif count == size_row-1:
            print(f"Linha:: {i}  >-1<")
        lista_verificadora.append(x)
        count +=1
    lista_verificadora.clear()
