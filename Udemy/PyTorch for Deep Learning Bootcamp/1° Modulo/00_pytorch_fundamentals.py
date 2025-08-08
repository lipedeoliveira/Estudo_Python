import os
os.system('clear')
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print(torch.__version__)


##Introduction to tensor

### Creating tensor
## The first tensor that we are going to create it's called scalar, (é um 'vetor' sem índices)
## PyTorch tensor are created using 'torch.tensor()' https://docs.pytorch.org/docs/stable/tensors.html
scalar = torch.tensor(7)
print(scalar.ndim)

#Get tensor back as python int
print(scalar.item())

#Vector
vector = torch.tensor([7,7])
print(vector.ndim) # The command vector.ndim return's 1 as result, because [7,7] has just 1 bracket

print(vector.shape)
#But, vector.shape return's 2, because, there are 2 numbers inside the 1 bracket

#Matrix
matrix = torch.tensor([[7,8],
                       [9,10]
                       ])

print(matrix)
print(matrix.ndim)
print(matrix.shape)

#TENSOR
TENSOR = torch.tensor([
                        [
                            [1,2,3],
                            [4,5,6],
                            [7,8,9]
                        ]
                    ])
print(TENSOR)
print(TENSOR.ndim)
print(TENSOR.shape)
## Ao rodar o print(TENSOR.shape), ele retorn a'torch.Size([1,3,3])', o que a primeira momento
## se mostra estranho depois de se ter conhecimento de scalar,vetor e matrix, contudo, o
## '1' em [1,3,3] se refere ao primeiro par de [], que está indicando o número de matrizes,ou
## seja, 1 matrix 3x3, o primeiro '3' se refere ao número de linhas, e o último 3, se refere a
## o número de colunas

## É comum que ao escrever váriaveis que representem scalar() ou vetores()
## as escreva em lowercase, contudo, quando se escreve alguma váriavel que
## represente uma matrix() ou um tensor(), a coloque em uppercase

### Random Tensor
"""
Why random tensors?

Random tensors are important because the way many neural networks learn is that
they start with tensor full of ramdom numbers and the adjust those random number
to better represent the data
 #ANCHOR: Start with random numbers -> look at data -> update random numbers -> look at data ->update random numbers
"""

# shape and size are the same thing to torch
#Creating a random tensor of size(3,4)
random_tensor = torch.rand(3,4)
print(random_tensor)

#ANCHOR Creating a raondom tensor with a similar shape to an image tensor
random_image_size_tensor = torch.rand(size=(3,224,224)) # colour channels(R,GB), height,width
print(random_image_size_tensor.shape,random_image_size_tensor.ndim)
# print(random_image_size_tensor)

#ANCHOR - Creating tensors of zero and one, it's usefull to create masks
zero = torch.zeros(size=(3,4))
print(zero)
print(zero * random_tensor)

#Creating a tensor full of ones
ones = torch.ones(size=(3,4))

print(ones.dtype)


#ANCHOR: Creating a range of tensor and tensor-like
one_to_ten = (torch.arange(start=1,end=11,step=1)) #https://docs.pytorch.org/docs/stable/generated/torch.arange.html
print(one_to_ten)

#Creating tensor like
#Criando um tensor com o formato/shape igual ao one_to_ten, mas no caso, cheio de zeros
ten_zeros = torch.zeros_like(input=one_to_ten)
print(ten_zeros)

#ANCHOR -  Tensor datatypes
    #Float 32 tensor
    #!SECTION  Nota:
"""
    Nota: Os tipos de dados dos tensores, são um dos 3 principais erros que se é enfrentado
            ao usar PyTorch & Deep Learning
            1. Os tensores não estarem com o tipo certo de dado
            2. Os tensores não terem o shape/formato correto
            3. Os tensores não estarem no dispositivo correto
"""
float_32_tensor = torch.tensor([3.0,6.0,9.0],
                               dtype=None,# dtype define qual o tipo é o tensor(e.g float32 ou float16)
                               device = None,#EM que dispositivo está o seu tensor

                               requires_grad=False)# Se vai ou não, acompanhar os gradientes com as operações deste tensor

print(float_32_tensor)
float_16_tensor = float_32_tensor.type(torch.float16)
print(float_16_tensor)

float_half_tensor = torch.tensor([12.0,15.0,18.0],dtype=torch.float16,device=None)
print(float_half_tensor)
