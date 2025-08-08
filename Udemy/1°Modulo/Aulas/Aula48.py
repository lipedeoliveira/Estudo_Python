"""
Desempacotamento em chamadas
de metódos e funções

"""

string = "ABCD"
listas_nomes = [
                ['Enzo','Joao'],
                ['Rodrigo','Gu'],
                ['Nino','Nico']
                
                ]
tupla = "Python","é","Legal"

# Pegando o primeiro, segundo item, pulando todos e depois pegando o último item da tupla
# # Colocar o * pega todos os itens que não foram listados
# primeiro,segundo, *resto,ultimo = lista

# print(primeiro,resto)

# print(*lista) # = for nome in lista: print(nome, end=' ')

print(*tupla,sep='-')
print(*listas_nomes,sep='\n')