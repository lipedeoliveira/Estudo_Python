"""
Iterável -> str,range, etc -> O elemento que possui outros elementos dentro
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador    

iter entrega um objeto interador    
"""     


#for letra in texto
texto = ("felipe") #Iterável
iterador = iter(texto)  #iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
#