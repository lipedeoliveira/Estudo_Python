#Exercicios com funções

#Crie uma função que multiplica todos os argumentos
#Não nomeados recebidos
#Retorne o total para uma variável e mostre o valor da variável


#Crie uma função que fala se um número é par ou ímpar
#Retorne se o número é par ou ímpar
#------------------------#
"""
def multiplicacaoNaoNomeada(*args):
    totalMultiplicacao = 1
    for numero in args:
        if type(numero) == str:
            try:
                numero = float(numero)
                totalMultiplicacao *= numero
            except:
                continue
    return totalMultiplicacao

entradaArgumentos =  tuple(input("Insira os números a serem multiplicados"))

resultadoMultiplicacao = multiplicacaoNaoNomeada(*entradaArgumentos)
print(resultadoMultiplicacao)
"""

def parImpar(x):
    try:
        x = float(x)
        if x % 2 == 0:
            return "O número é par"
        else:
            return "O número é ímpar"
    except:
        if type(x) == str:
           return "Foi inserido um caractere não númerico"

numeroInserido = input('Insirar o número a se saber se é par ou ímpar:: ')
resultadoVerificacao = parImpar(numeroInserido)
print(resultadoVerificacao)
