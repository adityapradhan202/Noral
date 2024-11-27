# This scripts is for making prediction... using the effnetb0 model
import os
import torchvision
import pathlib
import torch
from torch import nn
from PIL import Image
from torchvision import transforms

# Device agnostic code.
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

# Model dict path.
effnet_model_savepath = pathlib.Path('models/effnetb0_dict.pth')

# Class names list.
class_names = ['Caries', 'Gingivitis', 'Hypodontia', 'Mouth_ulcer', 'Tooth_discoloration']

loaded_effnet_weights = torchvision.models.EfficientNet_B0_Weights.DEFAULT
loaded_effnet_model = torchvision.models.efficientnet_b0(
    weights=loaded_effnet_weights
)

effnet_transform = loaded_effnet_weights.transforms()

for param in loaded_effnet_model.features.parameters():
    param.requires_grad = False

loaded_effnet_model.classifier = nn.Sequential(
    nn.Dropout(p=0.2, inplace=True),
    nn.Linear(in_features=1280, out_features=len(class_names), bias=True)
).to(device=device)

# Load the dict.
loaded_dict = torch.load(f=effnet_model_savepath, weights_only=True)
loaded_effnet_model.load_state_dict(loaded_dict)
loaded_effnet_model.to(device=device)

def predict_image(model:nn.Module,
                  img_path:str, 
                  model_transform:transforms,
                  device:torch.device=device):
    """A function to make predictions on custom images downloaded from the internet."""
    image_tensor = model_transform(Image.open(img_path))
    image_tensor = image_tensor.unsqueeze(dim=0)
    
    model.to(device=device)
    model.eval()
    with torch.inference_mode():
        logit = model(image_tensor.to(device))
        output = class_names[torch.softmax(logit, dim=1).argmax(dim=1).item()]

        return output

if __name__ == "__main__":
    predicted_class_name = predict_image(
        model=loaded_effnet_model,
        img_path='sample_images/Gingivitis_(crop).jpg',
        model_transform=effnet_transform,
        device="cpu" # Do prediction on cpu.
    )
    print(predicted_class_name)
