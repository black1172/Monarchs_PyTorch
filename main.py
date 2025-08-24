import view_data as vd
import load_sattelite_images as lsd
import matplotlib.pyplot as plt
import rasterio
from model import MonarchHabitatResNet50 as MHR
import torch
import calculate_patches as cp
import generate_patches as gp

# -------------------------------
# Configuration
# -------------------------------
patch_size = 128
num_of_images = 1
channels = 4
filename = "test\\m_3908453_se_16_1_20130924_20131031.jp2"
# -------------------------------

def main():
    print(f"Ready to work with: {filename}")

    # Model setup
    habitat_model = MHR(
        num_classes=8, 
        in_channels=4  # 4 channels for RGB + NIR data
    )
    habitat_model.eval()

    # Load image and convert to tensor
    satellite_tensor = lsd.load_satellite_image_as_tensor(filename).float()
    print(f"Satellite tensor shape: {satellite_tensor.shape}")

    # NOTE: satellite_tensor is expected to be [4, H, W]

    # Create patch batches
    patch_batch = gp.gen_patches_overlapping(satellite_tensor, patch_size)
    print(f"Batch shape: {patch_batch.shape}")

    # NOTE: patch_batch is expected to be [N, 4, H, W]

    # Add batch dimension
    satellite_tensor = satellite_tensor.unsqueeze(0)
    print(f"Tensor shape with batch: {satellite_tensor.shape}")
    
    # Calculate number of patches
    num_of_patches = cp.calculate_patches(satellite_tensor, patch_size)

    # Format into batches
    batches = torch.tensor([num_of_images, num_of_patches, channels, patch_size, patch_size]).float()
    print(f"Patches batch shape: {batches.shape}")
    batches = torch.stack((batches, patch_batch), dim=0)

    # Run inference on each patch
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

if __name__ == "__main__":
    main()