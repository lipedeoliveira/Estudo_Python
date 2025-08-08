# lista = [10,20,30,40]
# print(lista)
# lista.append(50) #Adiciona o novo valor, ao final do vetor ( lista )
# lista.pop() # A função pop() remove o último indice adicionado
# lista.append(60) #Adiciona o novo valor, ao final do vetor ( lista )
# print(lista)

"""
    append() - adiciona um item ao final do vetor
    insert( 'indice onde o item deve ser adicionado', 'valor a ser adicionado') - adiciona um item baseado no indice passado
    pop() - Remove o último indice ou o escolhido
    del() - Apaga um indice
    clear() - limpa a lista
    extend() - Extende a lista

    + - concatena listas


"""

lista = [10,20,30,40]
lista.append("Arroz")
nome = lista.pop()
lista.append(1234)
del lista[-3]
print(nome)
print(lista)




# print(lista)
# #A função del exclui um indice de dentro do vetor
# del lista[1]
# print(lista)
# Tomar cuidado com excluir itens no inicio de um vetor muito grande#
# Passar um índice dentro da chamada da função pop() permite escolher o indice dentro do vetor que será excluido