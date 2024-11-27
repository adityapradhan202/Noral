from flask import Flask, jsonify, request
import requests
from PIL import Image
import io

import torch
import torchvision
from torch import nn
from pathlib import Path
from torchscript import model_builder
from torchvision import transforms

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

class_names_effnet = ['Caries', 'Gingivitis', 'Hypodontia', 'Mouth_ulcer', 'Tooth_discoloration']
class_names_vgg = ['not_teeth', 'teeth']


# Loading the vgg model
model_vgg = model_builder.TinyVGG(
        input_shape=3,
        hidden_units=15,
        output_shape=1
).to(device=device)

vgg_transform_pipeline = transforms.Compose([
    transforms.Resize(size=(64,64)),
    transforms.ToTensor() 
])

loaded_state_dict_vgg = torch.load(f='models/vgg_binary.pth', weights_only=True)
model_vgg.load_state_dict(loaded_state_dict_vgg)



# Loading the effnet model
model_save_path = Path('models/eff2_model97.pth')

loaded_eff2_weights = torchvision.models.EfficientNet_B0_Weights.DEFAULT
loaded_eff2_model = torchvision.models.efficientnet_b0(
    weights=loaded_eff2_weights
).to(device=device)

for param in loaded_eff2_model.features.parameters():
    param.requires_grad = False

for param in loaded_eff2_model.features[-1].parameters():
    param.requires_grad = True

loaded_eff2_model.classifier = nn.Sequential(
    nn.Dropout(p=0.2, inplace=True),
    nn.Linear(in_features=1280, out_features=5, bias=True)
).to(device=device)

loaded_eff2_dict = torch.load(f=model_save_path, weights_only=True)
loaded_eff2_model.load_state_dict(loaded_eff2_dict)

effnet_transform_pipeline = loaded_eff2_weights.transforms()


# API code below
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error":"no file provided"})
    
    file = request.files['file']
    if file:
        image = Image.open(io.BytesIO(file.read()))

        img_tensor_vgg = vgg_transform_pipeline(image)
        img_tensor_vgg = img_tensor_vgg.unsqueeze(dim=0).to(device)
        img_tensor_effnet = effnet_transform_pipeline(image)
        img_tensor_effnet = img_tensor_effnet.unsqueeze(dim=0).to(device)

        model_vgg.to(device=device)
        loaded_eff2_model.to(device=device)

        model_vgg.eval()
        with torch.inference_mode():
            logit1 = model_vgg(img_tensor_vgg)
            pred_prob1 = torch.sigmoid(logit1)
            pred_label1 = torch.round(torch.sigmoid(logit1)).type(torch.int32).item()
            pred_class_vgg = class_names_vgg[pred_label1]
        
        loaded_eff2_model.eval()
        with torch.inference_mode():
            logit2 = loaded_eff2_model(img_tensor_effnet)
            pred_prob2 = torch.softmax(logit2, dim=1)
            index = torch.argmax(pred_prob2, dim=1).item()
            pred_class_effnet = class_names_effnet[index]

        results = {
            "TINY-VGG":pred_class_vgg,
            "EFFNET":pred_class_effnet
        }

        return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

