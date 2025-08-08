"""
conIntrodução ao desempacotamento + tuples(tuplas)
Tipo tupla, uma lista imutável


"""

#Pegando somente o primeiro valor

#Para declarar uma váriavel do tipo tupla, basta declarar uma lista sem colchetes
nomes = 'Joao','Arroz','Teste'
#Para ser mais especifico, basta declarar da mesma forma, contudo dentro de parenteses

nome1,*_ = ['Joao','Rebeca','Mateus','Julia']

print(nome1)


string = "ABCD"
lista = ['Maria','Helena',1,2,3,'Eduarda']

tupla = "Python","é","Legal"

# Pegando o primeiro, segundo item, pulando todos e depois pegando o último item da tupla
# Colocar o * pega todos os itens que não foram associados
primeiro,segundo, *resto,ultimo = lista

print(primeiro,resto)