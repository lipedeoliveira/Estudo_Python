"""

    Interpolacao basica de strings

    s - string
    d e i - int
    f - float
    x e X - Hexadecimal(ABCDEF0123456789)

"""

nome = 'Felipe'
preco = 1000.95897643
variavel = '%s, o preco e R$%f'% ( nome, preco)
print(variavel)
print('O hexadecimal de %d e %04X'%(1000,1000))