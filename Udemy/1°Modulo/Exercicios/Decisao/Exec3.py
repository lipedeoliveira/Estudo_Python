valor_1 = float(input("Insira um valor:\t"))
valor_2 = float(input("Insira outro valor:\t"))

valor3=(float(valor_1+valor_2))
 
if valor3>25:
    print(f"O resultado da soma de {valor_1} + {valor_2} equivale a um numero maior que 25, numero esse que é: {valor3}")

else:
    print(f"O resultado da soma de {valor_1} + {valor_2} equivale a um numero inferior que 25, numero esse que é: {valor3}")