import torch
import torchgeo
from torchgeo.models import ResNet50_Weights

# Load pre-trained model for satellite imagery
model = torchgeo.models.resnet50(weights=ResNet50_Weights.SENTINEL2_ALL_MOCO)

# Modify for your 4-band NAIP data
model.conv1 = torch.nn.Conv2d(4, 64, kernel_size=7, stride=2, padding=3, bias=False)

# Modify output for your habitat classes
model.fc = torch.nn.Linear(model.fc.in_features, 8)  # 8 habitat classes