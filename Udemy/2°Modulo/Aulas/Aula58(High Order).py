"""
High Order Functions
Funções de primeira classe
"""


def saudacao(msg):
    return msg

saudacao_2 = saudacao
v = saudacao_2('Bom dia')
print(v)

