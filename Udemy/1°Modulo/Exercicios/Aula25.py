"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# try:
#  numero_digitado = (input("Insira um número inteiro: "))
 

#  is_float = numero_digitado.isdigit()

#  if is_float == False:
#   numero_digitado = float(numero_digitado)
#   print("Isto não é um número inteiro ")

#  elif is_float == True:
#   numero_inteiro = int(numero_digitado) 
#   if numero_inteiro%2 == 0:
#       print("Número par")
  
#   elif numero_inteiro%2!=0:
#      print("Número Impar")

# except:
#     print("Isto não é um número ")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# try:
#  horario=int(input("Informe que horas são: "))
 
#  manha =  horario >=0 and horario <=11
#  tarde = horario >=12 and horario <=17
#  noite = horario >18 and horario <23

#  if manha:
#    print("Bom Dia")

#  elif tarde:
#    print("Boa tarde")

#  elif noite:
#    print("Boa noite")
 
#  else:
#    print("Número informado fora do padrão de 24 horas")
# except:
#  print("Formato inválido")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

try:
 
 nome = (input("Insira seu primeiro nome:  "))
 
 nome_numero = nome.isdigit()
 nome = len(nome)
 nome_curto = nome <=4
 nome_padrao = nome >=5 and nome <=6
 nome_longo = nome >6

 if nome_numero == False:
  if nome_curto :
    print("Você possui um nome curto")
  elif nome_padrao:
    print("Seu nome possui a quantidade de caracteres padrão")
  elif nome_longo:
    print("Seu nome é muito grande")
 else:
    print("Número Inserido")
except:
   print("Formato inserido invalido ")