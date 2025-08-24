import requests
import os
import numpy as np
import rasterio
import matplotlib.pyplot as plt
import torch

def visualize_bands(filename):
    with rasterio.open(filename) as src:
        data = src.read()  # Shape: (4, height, width)
        
        # Create a plot with all 4 bands
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        axes = axes.flatten()
        
        band_names = ['Band 1', 'Band 2', 'Band 3', 'Band 4']
        
        for i in range(4):
            axes[i].imshow(data[i], cmap='gray')
            axes[i].set_title(f'{band_names[i]}')
            axes[i].axis('off')
        
        plt.tight_layout()
        plt.show()
        
        # Also create RGB composite (if bands 1,2,3 are RGB)
        rgb_image = np.transpose(data[:3], (1, 2, 0))  # Convert to (H, W, C)
        
        plt.figure(figsize=(10, 8))
        plt.imshow(rgb_image)
        plt.title('RGB Composite')
        plt.axis('off')
        plt.show()

def confirm_nir_band(filename):
    with rasterio.open(filename) as src:
        data = src.read().astype(float)
        
        # NAIP typically: Band 1=Red, Band 2=Green, Band 3=Blue, Band 4=NIR
        red = data[0]   # Band 1 
        nir = data[3]   # Band 4 (your guess)
        
        # Calculate NDVI
        ndvi = (nir - red) / (nir + red + 1e-8)
        
        print(f"Using Band 1 (Red) and Band 4 (NIR):")
        print(f"NDVI range: {ndvi.min():.3f} to {ndvi.max():.3f}")
        print(f"NDVI mean: {ndvi.mean():.3f}")
        
        # Save NDVI image
        plt.figure(figsize=(8, 6))
        plt.imshow(ndvi, cmap='RdYlGn', vmin=-0.5, vmax=1.0)
        plt.title('NDVI (Red-Yellow-Green = Low-Medium-High Vegetation)')
        plt.colorbar()
        plt.savefig('ndvi_test.png')
        plt.close()
        print("Saved ndvi_test.png")
        
        return data

def gen_patches(satellite_tensor):
    # The full image shape: (4, H, W)
    print(f"The full image shape: {satellite_tensor.shape}")

    # Break the image into smaller patches and create a batch
    patch_batch = []
    height = 0
    width = 0

    # Generate patches
    while height < satellite_tensor.shape[2]:
        while width < satellite_tensor.shape[3]:
            patch = satellite_tensor[:, height:height+128, width:width+128]
            patch_batch.append(patch)
            width += 128
        height += 128
        width = 0

    return torch.unsqueeze(patch_batch, 0)  # Return a batch

def examine_satellite_data(filename):
    print(f"\nExamining {filename}...")
    
    # Open the satellite file
    with rasterio.open(filename) as src:
        data = src.read()  # This reads all the bands

        # Print basic information about the data
        print(f"Data shape: {data.shape}")
        print(f"Data type: {data.dtype}")
        print(f"Min value: {data.min()}")
        print(f"Max value: {data.max()}")