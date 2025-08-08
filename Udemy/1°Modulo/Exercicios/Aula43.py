MANTER = False
lista = []

while MANTER != True:
    escolha = input("\nSelecione uma opção\n[i]nserir [a]pagar [l]istar:: ")
        
    if escolha == "i":
        inserccao = input("\nInsira o nome do produto:: ")
        lista.append(inserccao)        

    elif escolha == "a":
      try:
         valor=(int(input("\nEscolha um indice para apagar:: ")))
         del lista[valor]
         print("\nIndice apagado\n")  
     #ValueError captura os exceptions de erro de valor de variavel
      except ValueError:
            print("Insira um valor númerico")
    #IndexError captura os erros de indices em listas
      except IndexError:
          print("Indice inexistente")

    
    if escolha == "l":
        if len(lista) == 0:
            print("\nNada para listar\n")
            continue
        for indice,nome in enumerate(lista):
            print(indice,nome)        
    
    