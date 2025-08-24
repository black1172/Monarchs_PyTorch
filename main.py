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
print(f"Satellite tensor shape: {satellite_tensor.shape}")

# NOTE: Tensor shape is [4, H, W]

satellite_tensor = satellite_tensor.unsqueeze(0)  # Add list dimension

# NOTE: Tensor shape is [1, 4, H, W]

patches_batch = vd.gen_patches(satellite_tensor).float()
print(f"Patches batch shape: {patches_batch.shape}")

# Create batches
batches = torch.empty(0, 4, 128, 128).float()
batches = torch.cat((batches, patches_batch), dim=0)

print(f"Batch shape: {batches.shape}")

for patch_batch in batches:
    with torch.no_grad():
        try:
            output = habitat_model(patch_batch)
            print("Model works!")   
            
            probabilities = torch.softmax(output, dim=1)
            predicted_class = torch.argmax(probabilities, dim=1)
            
            print(f"Predicted habitat: {habitat_model.habitat_classes[predicted_class.item()]}")
            
        except Exception as e:
            print(f"Error: {e}")