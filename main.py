import view_data as vd
import load_sattelite_images as lsd
import matplotlib.pyplot as plt
import rasterio
from model import MonarchHabitatResNet50 as MHR
import torch

filename = "test\m_3908453_se_16_1_20130924_20131031.jp2"
print(f"Ready to work with: {filename}")

# Create model instance
habitat_model = MHR(
    num_classes=8, 
    in_channels=4  # Important: 4 channels for RGB + NIR data
)
habitat_model.eval()  # Set to eval mode

# load and split up image into smaller tensors
satellite_tensor = lsd.load_satellite_image_as_tensor(filename).float()
test_batch = vd.test_patch(satellite_tensor).float()

# Create batches
batches = []
batches.append(test_batch)

for test_batch in batches:
    with torch.no_grad():
        try:
            output = habitat_model(test_batch)
            print("Model works!")
            
            probabilities = torch.softmax(output, dim=1)
            predicted_class = torch.argmax(probabilities, dim=1)
            
            print(f"Predicted habitat: {habitat_model.habitat_classes[predicted_class.item()]}")
            
        except Exception as e:
            print(f"Error: {e}")