"""
enumerate - enúmera iteráveis (indices)

"""
lista = ['Maria','Joao','Pedro']
lista.append("Macarrão")

#lista_enumerada = enumerate(lista)

#for indices in enumerate(lista):
#   indice, nome = indices
#   print(indice,nome) 
    
#Faz o mesmo que acima
for indice,nome in enumerate (lista):
    print(indice, nome)