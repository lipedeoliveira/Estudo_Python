
# O ; serve para a separação de instruções, permitindo escrever várias em uma só linha

variavel1 = True;variavel2 = False;print(variavel2,"\n")

# É possível atribuir o mesmo valor para várias váriaveis em somente uma linha

a = b = c = 10


#Listas de compreensão
#As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente. Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.


números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 
            for x in números 
            if x % 2 == 0
            ]
print(quadrados)  # Imprime [4, 16]


"""


"""

#Criação de Dicionários

pessoa = {"nome":"Joao","Idade":"25","cidade":"Madri"}

print(pessoa["nome"])
print(pessoa["Idade"])
print(pessoa["cidade"])


#Metodos de Dicionários

"""
keys(): Retorna uma visualização de todas as chaves do dicionário
values(): Retorna uma visualização de todos os valores do dicionário
items(): Retorna uma visualização de todos os pares chave-valor do dicionário
update(outro_dicionário): Atualiza o dicionário com os pares chave-valor de outro dicionário

"""

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
pessoa.update({"Profissão":"Engenheiro"})

print(pessoa)


#Criação e operações básicas

numeros = set([1,2,3,4,5])

conjunto1 = {1,2,3}
conjunto2 = {4,5,6}

uniao = conjunto1 | conjunto2
print(uniao) #Imprime {1,2,3,4,5}

intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca) #Imprime {1,2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)