"""
CPF: 746.824.890-70

Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma contagem
regressiva começando de  10

Ex: 746.824.890-70

    10 9  8  7  6  5  4  3  2 
    
 *  7  4  6  8  2  4  8  9  0
    
    70 36 48 56 12 20 32 27 0 

Somar todos os resultados

70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado por 10
301*10 = 3010

Obter o resto da divisão da conta anterior por 11

3010%11 = 7

Se o resultado anterior for maior que 9:
    resultado é 9

contrário disso:
    Resultado é o valor da conta
"""
import os
os.system("cls")
cpfFormatado = []
cpfCru = input("Insira o CPF:: -> ")

while len(cpfCru) >14 or len(cpfCru)<11:
    cpfCru = input("Erro: Excedeu a quantidade de caracteres\nInsira o CPF:: -> ")
    #Esse for é responsável por capturar somente os números, e excluir outros caracteres


    
for i in cpfCru : 
    try:
        if len(cpfFormatado)<=8:
            cpfFormatado.append(int(i)) 
    except ValueError:
        ...       

    tamanhoCPF = 9
    cpfCalculado = 0
    i = 0
    c = 10
#220 824 898 8
cont = 0
condicao_Incrementavel = 2
while cont < 2 :
    cont +=1            
    while c >=condicao_Incrementavel :
        cpfCalculado += cpfFormatado[i]*c
        c-=1
        i +=1
        
        
    cpfCalculado = (cpfCalculado*10)%11
    cpfFormatado.append(cpfCalculado if cpfCalculado <=9 else 0)
    c = 11
    i = 0
    condicao_Incrementavel = 3
    cpfCalculado = 0


print(cpfFormatado)

"""
Calculo do segundo digito do CPF
CPF:Ex: 746.824.890-70

Colete a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma contagem
regressiva começando de 11

Ex: 746.824.890-70

    11 10 9  8  7  6  5  4  3  2

    7  4  6  8  2  4  8  9  0  7 <-- Primeiro digito
    
    77 40 54 64 14 24 40 36 0 14
    
    568.706.578.40
    Somar todos os resultados = 363
    
    Multiplicar o resultado anterior por 10
    
    363*10 = 3630
    
    Obter o resto da divisão de 3.630%11
    
    = 0
    
    Se o resultado anterior for maior que 9:
        Resultado é 0
        
    Contrário:
        Resultado é o valor da conta
"""


