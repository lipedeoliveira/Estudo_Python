"""

Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)


"""
def soma(x,y):
    
    result = f"{x=} {y=} I x+y = {x+y}"
    return result    

print(soma(x=2,y=1))