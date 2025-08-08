"""
Manipulando dicionários
"""
pessoa = {}
chave = 'nome'
#Criando um índice dentro do dicionário
pessoa[chave] = 'Felipe'
pessoa['Sobrenome'] = "Vieira"
del pessoa['Sobrenome']
print(pessoa['nome'])
