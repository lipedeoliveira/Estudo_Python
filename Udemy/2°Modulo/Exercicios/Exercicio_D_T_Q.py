"""
Exercicio
Crie funções que duplicam, triplicam e quadriplicam
o número recebido como parâmetro
"""

def mulitplicacao(valor):
    def duplicar():
        return valor*2
    def triplicar():
        return valor*3
    def quadriplicar():
        return valor*4

    return (duplicar(),triplicar(),quadriplicar())

v = mulitplicacao(2)
print(v)
