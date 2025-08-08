"""
Valores padrão para parâmetros

Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.

Refatorar--> Editar o seu código
      
    
"""

def soma(x, y, z = None ):
    if z is not None:
        print("\nO terceiro valor foi enviado")       
        print(f'{x=} {y=} {z=}',x+y+z)
    else:
        print("O terceiro valor não foi enviado")
        print(f'{x=} {y=} {z=}',x+y+z)

soma(1,2,3)