"""
    Operador lógico "not"
    usado para inverter expressoes
    not True = False
    not False = True
"""
print(not True) #False
print(not False) #True


senha = input('Senha:')

if not senha:
    senha = input('Voce nao digitou nada, insira sua senha')