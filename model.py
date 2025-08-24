import torch
import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights

class MonarchHabitatResNet50(nn.Module):
    def __init__(self, num_classes=8, in_channels=3):
        super().__init__()
        self.model = resnet50(weights=ResNet50_Weights.DEFAULT)
        print("Loaded ImageNet pre-trained ResNet50")

        self.model.conv1 = nn.Conv2d(
            in_channels=in_channels,
            out_channels=64,
            kernel_size=7,
            stride=2,
            padding=3,
            bias=False
        )

        self.model.fc = nn.Linear(
            in_features=self.model.fc.in_features,
            out_features=num_classes
        )

        # Define class mapping
        self.habitat_classes = {
            0: "Grassland/Prairie",
            1: "Wetland/Riparian",
            2: "Agricultural/Cropland",
            3: "Forest Edge",
            4: "Urban/Suburban",
            5: "Water Bodies",
            6: "Developed/Roads",
            7: "Other/Barren"
        }

    def forward(self, x):
        return self.model(x)

