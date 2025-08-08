import torch

#CRIANDO UM TENSOR COM SOMENTE UMA COLUNA
a = torch.ones(5) #Que comando engrançado, é literalmente um comando para  vc repetir o número um e depois tu passa a quantidade de vezes

print (a)


#CRIANDO UM TENSOR COM COM SOMENTE ZEROS EM UMA COLUNA
b = torch.zeros(5)
print(b)

#CRIANDO UM TENSOR COM VALORES CUSTOMS

c = torch.tensor([1.0,2.0,3.0,4.0,5.0])
print(c)

#               l,c
d = torch.zeros(3,2)
print(d)

e = torch.ones(3,2)
print(e)

f = torch.tensor([[1.0,2.0],[3.0,4.0]])
print(f)

#Tensor 3D
g = torch.tensor([[[1.,2.],[3.,4.],[5.,6.],[7.,8.]]])
print(g)

#Também dá pra achar o tamanho do tensor usando método .shape
print(e.shape)
print(f.shape)
print(g.shape)
#-------#

#Acessando elementos nos tensores
#Pegando um elemento no index 2
print(c[2])

#Pegando um elemento na linha 1 , coluna 0
print(f[1,0])

#Todos os elementos
print(f[:])

#Todos os elementos de 1 a 2(excluindo o elemento )
print(c[1:3])

#TOdos os elementos até o index 4 
print(c[:4])

#Primeira linha
print(f[0,:])

#Segunda coluna
print(f[:,1])
