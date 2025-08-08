for i in range(10):
    if i == 2:
        print(f'i é {i}, pulando...')
        continue
    if i == 8:
        print(f'Seu i é {i}, seu else não executara')
        break
    for j in range(1,3):
        print(i,j)
else:
    print("For completo com sucesso")