"""
Split e join com list e str
slipt - divide uma str
join - une uma str
strip - corta os espaços iniciais e finais
"""

frase = "     Arroz com, feijão é bom      "

#lista_palavras = frase.split("aqui vai o divisor, onde vai ser dividio")

lista_palavras_crua = frase.split(",")
lista_palavras_fixed = []
for i,frase in enumerate(lista_palavras_crua):
    lista_palavras_fixed.append(lista_palavras_crua[i].strip())
# print(lista_palavras_fixed)
# # print(lista_palavras_crua)

#Somente iteráveis
frases_unidas = "-".join(lista_palavras_fixed)
print(frases_unidas)