frase = 'Bolhas bolhudas tem formato de bola, já que bolas feita de sabão'

i = 0

letra_apareceu_mais = ""
qntd_letras = 0
qntd_letras_temp = 0
tamanho_frase = len(frase)

while i < tamanho_frase:
    
    letra_atual = frase[i]
    i+=1

    qntd_letras_temp = frase.count(letra_atual)
    if letra_atual == " ":
        continue
    if qntd_letras<qntd_letras_temp:
        qntd_letras = qntd_letras_temp
        letra_mais_apareceu = letra_atual
        letra_apareceu_mais = qntd_letras_temp


print(f'A letra que mais apareceu foi a "{letra_mais_apareceu}"  e a quantidadede vezes que ela apareceu foi {letra_apareceu_mais}')
    
