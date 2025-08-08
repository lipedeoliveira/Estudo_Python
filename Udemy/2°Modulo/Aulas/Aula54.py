"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.

Existe o escopo global e local.

O Escopo global é o escopo onde todo o código é alcançável 
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados

"""

x =1 


def escopo():
    #global x se refere a edição de uma váriavel fora do escopo da função
    global x 
    print(x)
    
escopo()