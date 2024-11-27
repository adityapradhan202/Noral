# Prediction script for the vgg model that can do binary classification on whether an image is the image of teeth or not!

# Prediction script of the tiny vgg model.
# Accuracy is 74 percent on unseen data.

import torch
import torchvision
from torch import nn
import os
from pathlib import Path
from torchscript import model_builder
from torchvision import transforms
from PIL import Image

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

class_names = ['not_teeth', 'teeth']

model_vgg = model_builder.TinyVGG(
        input_shape=3,
        hidden_units=15,
        output_shape=1
).to(device=device)

transform_pipeline = transforms.Compose([
    transforms.Resize(size=(64,64)),
    transforms.ToTensor() 
])

loaded_state_dict = torch.load(f='models/vgg_binary.pth', weights_only=True)
model_vgg.load_state_dict(loaded_state_dict)

def predict(img_path:str, device:str,
        model:torch.nn.Module=model_vgg,
        transform_pipeline:torchvision.transforms=transform_pipeline):
    
    pil_img = Image.open(img_path)
    img_tensor = transform_pipeline(pil_img)
    img_tensor = torch.unsqueeze(img_tensor, dim=0)
    img_tensor.to(device=device)

    model.to(device=device)
    model.eval()
    with torch.inference_mode():
        raw_logits = model(img_tensor)

        pred_prob = torch.sigmoid(raw_logits).item()
        pred_prob = round(pred_prob, 2)
        pred_label = torch.round(torch.sigmoid(raw_logits)).type(torch.int32).item()
        pred_class = class_names[pred_label]

        return pred_class

if __name__ == "__main__":
    print(predict(img_path='sample_images/Gingivitis_(crop).jpg', device="cpu"))
    
    