"""
Exercicio
Pedir ao usuário para inserir o nome
Pedir ao usuário para inserir a idade

Caso ambos seja digitados, exibir:

    nome
    nome invertido
    nome tem x letras
    a primeira letra do nome
    seu nome contem ou nao, espacoes
    a ultima letra
Se nada for digitado:
    Desculpe, erro, nada foi digitado
"""

nome = input("Insira seu nome fazendo o favor:  ")
idade = input("Insira sua idade fazendo o favor:  ")

if nome and idade:
    print("Seu nome é ",nome)
    print("\nSua idade é",idade)
    print("\nSeu nome invertido é ",nome[::-1])
    print("\nseu nome tem ",len(nome)," caracteres")
    print("\nA primeira letra do seu nome é",nome[:1])
    print("\nA última letra do seu nome é ",nome[::len(nome)])
else:
    print("Desculpé, erro na digitação")
