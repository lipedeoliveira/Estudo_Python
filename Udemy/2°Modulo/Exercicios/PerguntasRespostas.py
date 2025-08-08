#Exercicios - sistema de perguntas e respostas
import copy
import os
os.system('clear')
perguntas = [
    {
        'Pergunta':'Quanto é 2+2 ?',
        'Opcoes':['1','2','3','4','5'],
        'Resposta':'4',
    },
        {
        'Pergunta':'Quanto é 5*5?',
        'Opcoes':['25','55','10','51','30'],
        'Resposta':'25',
    },
    {
        'Pergunta':'Quanto é 10/2 ?',
        'Opcoes':['4','20','1','5','10'],
        'Resposta':'5',
    }
]
dictTeste = {}
dictTeste = copy.deepcopy(perguntas[0])

for a in dictTeste:

    if a == 'Resposta':
        respostaUsuario = input("Qual a opção correta ?  ")

        if respostaUsuario == enumerate(dictTeste[a]):
            print("Certo")
            continue
        elif respostaUsuario != dictTeste[a]:
            print(f'Respota errada, o correto é : {dictTeste[a]}')
            continue

    if a == 'Opcoes':
        contador = 0
        for x in dictTeste[a]:
            print(f'{contador}) {x}\n')
            contador +=1
        continue

    print(a,dictTeste[a],'\n')

    ...

print(len(dictTeste))
# def rodarPerguntas():
#     x=0
#     dictT = {}
#     dictPerguntas = {}
#     v=''
#     for x in perguntas:
#        v += (f'{x}\n')
#     dictPerguntas = dict(v)
#     print(dictPerguntas)
# print(rodarPerguntas())
