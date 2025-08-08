import torch
import torch_directml

device = torch_directml.device()

print("Rodando loop")
x = torch.randn(512,512,device=device)
for i in range(10000):
	x = torch.sin(x @ x)
	print("Rodando o loop....")
print("Finalizado")
