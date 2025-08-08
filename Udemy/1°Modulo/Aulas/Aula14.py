#formatação de strings com format
a="A"
b="B"
c=1.132
teste = "a={0},b={1},c={2:.1f},d={0}"
formato=teste.format(a,b,c)
print(formato)
#nomeando os índices, parâmetro nomeado
teste2 = "a={0},b={1},c={nome3:.1f},d={0}"
formato2=teste2.format(a,b,nome3=c)
print(formato2)

