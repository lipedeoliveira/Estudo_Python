"""

     Formatação básica de strings
    s - string
    d e i - int
    f - float
    x e X - Hexadecimal

    (Caractere)(><^)(quantidade)

    > Esquerda
    < Direita
    ^ Centro

    Sinal -+ ou -

    Ex: 0>-100,.1f
    Conversion flags - !r !s !a

"""

variavel="ABC"

print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}.")
print(f"{variavel: ^10}")
print(f"{variavel:%>10}")