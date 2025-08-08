import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

# === Definição do mesmo modelo do treinamento ===
class SimpleCNN(nn.Module):
	def __init__(self):
		super(SimpleCNN, self).__init__()
		self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
		self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
		self.pool = nn.MaxPool2d(2, 2)
		self.fc1 = nn.Linear(32 * 32 * 32, 64)
		self.fc2 = nn.Linear(64, 1)

	def forward(self, x):
		x = self.pool(F.relu(self.conv1(x)))
		x = self.pool(F.relu(self.conv2(x)))
		x = x.view(-1, 32 * 32 * 32)
		x = F.relu(self.fc1(x))
		x = torch.sigmoid(self.fc2(x))
		return x

# === Carrega imagem ===
image_path = "imagem1.jpg"
image = Image.open(image_path).convert('RGB')

transform = transforms.Compose([
	transforms.Resize((128, 128)),  # Igual ao treinamento
	transforms.ToTensor(),
	transforms.Normalize([0.5], [0.5])
])

img_tensor = transform(image).unsqueeze(0)

# === Carrega modelo ===
model = SimpleCNN()
model.load_state_dict(torch.load("modelo_folha.pth", map_location="cpu"))
model.eval()

# === Inferência ===
with torch.no_grad():
	output = model(img_tensor)
	prediction = (output > 0.5).item()  # binário

print("É uma folha." if prediction == 0 else "NÃO é uma folha.")
