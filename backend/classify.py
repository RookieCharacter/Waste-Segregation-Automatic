import torch
from torchvision import transforms
from PIL import Image

dummy_labels = ["biodegradable", "plastic", "metal", "e-waste"]

# Dummy model class
class DummyModel:
    def eval(self): pass
    def __call__(self, x): return torch.randn(1, 4)

model = DummyModel()
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def classify_image(image_file):
    image = Image.open(image_file).convert("RGB")
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    return dummy_labels[predicted.item()]