import torch
import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights

# This definitely works - standard PyTorch
model = resnet50(weights=ResNet50_Weights.DEFAULT)
print("Loaded ImageNet pre-trained ResNet50")