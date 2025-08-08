"""
Calculadora simples
"""

print(f'{5*"-"}Calculadora{5*"-"}')

saida = None
operadoresPermitidos = "+-/*"

while not saida:

    try:

        primeiroNumero =float(input("\nInsira o primeiro número:: "))
        segundoNumero = float(input("Insira o segundo número:: "))
        
        operadorLogico = input("Insira o tipo de conta desejado:: ")


        if operadorLogico == '+' or operadorLogico == 'adição':
            resultado = primeiroNumero + segundoNumero
            print(f'O resultado da soma é {resultado}')

        elif operadorLogico == '-' or operadorLogico == 'subtração':
            resultado = primeiroNumero - segundoNumero
            print(f'O resultado da subtração é {resultado}')

        elif operadorLogico == '/' or operadorLogico ==  'divisão':
            resultado = primeiroNumero/segundoNumero
            print(f'O resultado da divisão é {resultado:.2f}')

        elif operadorLogico == '*' or operadorLogico == 'multiplicação':
            resultado = primeiroNumero*segundoNumero
            print(f'O resultado da multiplicação é {resultado}')
    

    except:
        print("Erro")
    

    permisaoOperadores = operadorLogico not in operadoresPermitidos or len(operadorLogico)>1

    if  permisaoOperadores:
            print("Operador inválido ou mais de um operador usadao para uma operação")    
            continue
 
    saida = input("\nDeseja Sair?\n").lower().startswith('s')

    if saida:
            break