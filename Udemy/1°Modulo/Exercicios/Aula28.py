nome = 'Felipe Vieira de Oliveira'
tamanhoNome = len(nome)
nomeNovo = " "

coluna = 0

while coluna<tamanhoNome:
    nomeNovo +=(f'*{nome[coluna]}')
    print(nomeNovo)
    coluna +=1