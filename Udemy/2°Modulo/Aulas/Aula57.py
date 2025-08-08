"""

args - Argumentos não nomeados
* - * args (empacotamento e desemapacotamento)
"""

#Lembrando do desempacotamento
x,y, *resto = 1,2,3,4,5


def soma(*args):

    total =0
    for numero in args:
        total += numero
        print(numero,total)
    return x+y


soma(1,2,3,4,5,6)

#sum() só recebe tuplas
print(sum((1,2,3,4,5,6,6,7,9,10)))

numeros = 1,2,3,4,5,6,7,8,9,10
soma(*numeros)
#Usando o * em numeros para desempacotar e enviar como números para função soma
