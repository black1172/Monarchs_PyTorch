import torch
import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights

# from torchgeo.models import ResNet50_Weights, resnet50  # torchgeo had too many dependencies for windows
model = resnet50(weights=ResNet50_Weights.DEFAULT)
print("Loaded ImageNet pre-trained ResNet50")

# look at the input layer
print("Original INPUT layer:")
print(f"  Type: {type(model.conv1)}")
print(f"  Input channels: {model.conv1.in_channels}")
print(f"  Output channels: {model.conv1.out_channels}")

# look at the output layer  
print("\nOriginal OUTPUT layer:")
print(f"  Type: {type(model.fc)}")
print(f"  Input features: {model.fc.in_features}")
print(f"  Output classes: {model.fc.out_features}")