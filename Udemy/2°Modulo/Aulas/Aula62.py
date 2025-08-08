# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1':1,
    'c2':2,
    'c3':3,
}
d2 = d1 # Isso só faz que d2 referencie o d1, ou seja, mudar o d2, muda o d1

d2 = copy.deepcopy(d1) # Deste forma, o conteudo de d1 é passado para d2 de forma profunda, o copy() sozinho faz uma copia "rasa"
d2['c1'] = 1000
print(d1 )
print(d2)
