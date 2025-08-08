"""Imprecisão de ponto flutuante

"""
import decimal
#A função Decimal() serve para números muito, muito precisos, e se passa uma String
#já que a função Decimal() faz conversão por si própriad
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1+numero_2
print(numero_3)

#round recebe o número que se deseja arredondar, e se passa o número de casas decimais 
print(round(numero_3,2))