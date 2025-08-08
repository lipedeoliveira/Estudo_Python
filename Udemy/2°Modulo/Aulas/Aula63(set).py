import os
os.system('clear')
"""
Sets - Conjunto em Python(tipo set)
Conjuntos são ensinados em matemática

Representados graficiamente pelo diagrama de Venn
Sets em python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno


#Criando um set()
set(iterável) ou {1,2,3}

Sets sao eficientes para remover valroes duplicados de iteráveis

 - ELes não tem indexes;
 - Eles não garantem ordem;
 - Eles são iteráveis (for, in, not in)

 Metodos úteis

    add, update, clear, discard
 """

# s1 = set() # = s1 = {'felipe',1,2,3,'vieira'}
# print (s1,type(s1))


s1 = {1,2,3,3,3,3,3,1} # O set exlui dados duplicados
print(s1)
