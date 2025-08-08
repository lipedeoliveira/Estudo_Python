import torch
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
import cv2

print("torch version: {}".format(torch.__version__))

digit_0_array_og = cv2.imread("mnist_0.jpg")
digit_1_array_og = cv2.imread("mnist_1.jpg")


#Modificando a imagem para um padrão de cinza para facilitar no processamento
digit_0_array_gray = cv2.imread("mnist_0.jpg",cv2.IMREAD_GRAYSCALE)
digit_1_array_gray = cv2.imread("mnist_1.jpg",cv2.IMREAD_GRAYSCALE)

#Visualizando a imagem
fig, axs = plt.subplots(1,2, figsize=(10,5)) #Definindo o tamanho da imagem

axs[0].imshow(digit_0_array_og,cmap='gray',interpolation='none')
axs[0].set_title("Digit 0 Image")
axs[0].axis('off')

axs[1].imshow(digit_1_array_og,cmap='gray',interpolation='none')
axs[1].set_title("Imagem do digito 1")
axs[1].axis('off')

#Array NumPy com três canais:
print("Image array shape: ",digit_0_array_og.shape)
print(f"Min pix value:{np.min(digit_0_array_og)}; Max pixel value: {np.max(digit_0_array_og)}")

#Convertendo um array do NumPy para um tensor
img_tensor_0 = torch.tensor(digit_0_array_og,dtype=torch.float32) /255.0
img_tensor_1 = torch.tensor(digit_1_array_og,dtype=torch.float32) /255.0

print("Shape of Normalised Digit 0 Tensor: ",img_tensor_0.shape)
print(f"Normalised Min pixel value: {torch.min(img_tensor_0)}; Normalised Max pixel value:{torch.max(img_tensor_0)}")

plt.imshow(img_tensor_0,cmap="gray")
plt.title("Normalised Digit 0 Image")
plt.axis('off')
plt.show()
