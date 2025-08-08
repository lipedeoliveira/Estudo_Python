"""
Fatiamento de Strings
 012345678
 Olá Mundo
-987654321

Fatiamento[i:f:p] [::]

i: = Inicio

f: = Fim

p: = Um passo da String


Obs.: a função 'len' retorna a quantidade de caracteres da String

"""

variavel = "Ola mundo"

print(variavel[4:]) #Irá printar a partir do 4° caractere até o final
print(variavel[:4])#Ira printar do começo até o terceiro caractere, já que o python não printa o 4° caractere

#Retorna a quantidade de caracteres
print(len(variavel[4:]))

#Irá printa do começo da String, até o tamanho dela ( no caso o final), e com passo de 2
# ( oque significa que ele irá printa um caractere, pular um, e printar o seguinte
print(variavel[0:len(variavel):2])
print(variavel[0:9:2])

# print(variavel[0:len(variavel):2]) = print(variavel[0:9:2])

#Printa a variavel ao contrário, pois printa do final ao começo
print(variavel[-1:-10:-1])
