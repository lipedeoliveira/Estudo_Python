#Whille/else

string = "valor"
i = 0
while i < len(string):
    letra = string[i]
    print(letra)

    if letra == " ":
        break
    i+=1
else:
    print("Não foi encontrado nenhum espaço")