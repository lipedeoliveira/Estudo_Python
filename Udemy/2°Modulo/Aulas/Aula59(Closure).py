"""
Closure e funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao},{nome}'
    return saudar #Ao nao fechar os () do retorno da função, acabo por obrigar o python a guardar tais valores e a função não é executada

s1  = criar_saudacao("bom dia")

print(s1)
#print(s1("Felipe")) #Ao colocar () na váriavel que recebe a função, eu termino de executar a função e isso é o Closure

for nome in ['Felipe','Luiz','Pedro','Joacielio']:
    print(s1(nome))
