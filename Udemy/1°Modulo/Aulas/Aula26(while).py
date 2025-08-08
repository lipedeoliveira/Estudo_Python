"""

Repetições
while(enquanto)
Executa uma ação enquanto uma condição for determinada como verdadeira0000000000000000000000000000000000

"""

# condicao= True
# while condicao:
#     nome = input("Qual o seu nome ?: ")
#     print(f'Seu nome é {nome}')
#     if nome == 'sair':
#         break # Encerra o loop
# print('Acabou')

"""
Operadores de atribuição
 =, +=, -=, *=, /=, //=, **=, %=   

"""


numero = 0 

while numero < 100000:
    numero +=1 # == numero = numero + 1

    if numero >= 50 and numero <=60:
        continue # serve para pular esta momento do loop, e ir para o próximo
    print(numero)

    if numero == 100:
        break
