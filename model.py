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

# Input model
model.conv1 = nn.Conv2d(
    in_channels=3,          # this is needed to match the number of input channels of the model
    out_channels=64, 
    kernel_size=7, 
    stride=2, 
    padding=3, 
    bias=False
    )

# look at the output layer  
print("\nOriginal OUTPUT layer:")
print(f"  Type: {type(model.fc)}")
print(f"  Input features: {model.fc.in_features}")
print(f"  Output classes: {model.fc.out_features}")

# Output model
model.fc = nn.Linear(
    in_features=model.fc.in_features,
    out_features=8         # this is needed to match the number of output classes
)