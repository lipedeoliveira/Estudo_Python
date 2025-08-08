"""
"""
import os
secret_word  = "tropeiro"
acertos = ""
numero_tentativas = 0
while True:
    letra_digitada = input("Insira ume letra:: ")
    numero_tentativas+=1
    if len(letra_digitada) > 1:
        print("Insira somente um caractere por vez:: ")
        continue
    
    if letra_digitada in secret_word:
        acertos += letra_digitada    

    palavra_formada = ""
    for letra_secreta in secret_word:
        if letra_secreta.lower() in acertos:
            palavra_formada+=letra_secreta
        else:
            palavra_formada+=("*")
    print(palavra_formada)
    
    if palavra_formada == secret_word:
        os.system('cls')
        print("VOCÊ GANHOU, PARÁBENS")
        print(f'A palavra secreta era: {secret_word}')
        print(f"A quantiadade de tentativas foi: {numero_tentativas}")
    
