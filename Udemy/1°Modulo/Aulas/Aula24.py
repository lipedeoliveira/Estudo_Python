"""
Flag - Marcar um local

id = identidade da váriavel dentro da memória

is e is not = é ou não é ( valido para : tipo, valor, identidade)


is é similiar ao ==, contudo o is é mais comumente usado com o none


"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Printar algo")
else:
    print(" A")

if passou_no_if is None:
    print("Não passou no if")

if passou_no_if is not None:
    print("Passou no if")