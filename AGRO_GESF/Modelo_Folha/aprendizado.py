import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets,transforms
import torch_directml


#Vendo qual peça tá sendo usada
device = torch_directml.device()
print(f"Usando:{device}")

x = torch.randn(1,3,128,128).to(device)
print(x.device)

transform = transforms.Compose([ 

	transforms.Resize((128,128)),
	transforms.ToTensor(),
	transforms.Normalize([0.5],[0.5]) #Serve pra normalizar entre -1 e 1
	
])

dataset = datasets.ImageFolder('dataset',transform=transform)

train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size

train_dataset,val_dataset = torch.utils.data.random_split(dataset,[train_size,val_size])
train_loader = DataLoader(train_dataset, batch_size=16,shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16,shuffle=True)

#Modelo Leve
class SimpleCNN(nn.Module):
	def __init__(self):
		super(SimpleCNN,self).__init__()
		self.conv1 = nn.Conv2d(3,16,3,padding=1)
		self.conv2 = nn.Conv2d(16,32,3,padding=1)
		self.pool = nn.MaxPool2d(2,2)
		self.fc1 = nn.Linear(32*32*32,64)
		self.fc2 = nn.Linear(64,1)

	def forward(self,x):
		x = self.pool(F.relu(self.conv1(x)))
		x = self.pool(F.relu(self.conv2(x)))
		x = x.view(-1,32*32*32)
		x = F.relu(self.fc1(x))
		x = torch.sigmoid(self.fc2(x))
		return x
model = SimpleCNN().to(device)

criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.001)


#Loop do treino de aprendizado
for epoch in range(100):
	model.train()
	running_loss= 0.0
	correct_train = 0
	total_train = 0
	
	for inputs,labels in train_loader:
		inputs = inputs.to(device)
		labels = labels.to(device).float().view(-1,1)

		optimizer.zero_grad()
		outputs = model(inputs)
		loss = criterion(outputs,labels)
		loss.backward()
		optimizer.step()

		running_loss +=loss.item()
		predicted = (outputs > 0.5).float()
		correct_train += (predicted == labels).sum().item()
		total_train += labels.size(0)

	train_loss = running_loss / len(train_loader)
	train_acc = 100* correct_train /total_train

	#Modo avaliação para validação
	model.eval()
	val_loss =0.0
	correct_val = 0
	total_val = 0
	
	with torch.no_grad():
		for inputs, labels in val_loader:
			inputs = inputs.to(device)
			labels = labels.to(device).float().view(-1,1)

			outputs = model(inputs)
			predicted = (outputs > 0.5).float()
			correct_val += (predicted == labels).sum().item()
			total_val += labels.size(0)

	val_loss /=len(val_loader)
	val_acc = 100 * correct_val / total_val

	print(f"Época {epoch+1} -" 
				f"Train Loss:{train_loss:.6f},Train Acc:{train_acc:.2f}% |"
				f"Val Loss: {val_loss:.6f}, Val Acc: {val_acc:.2f}%")


model.eval()
correct = 0
total = 0


print(f"Acurácia de validação: {100*correct/total:.2f}%")

torch.save(model.state_dict(),"modelo_folha.pth")
