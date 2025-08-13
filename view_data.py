import requests
import os
import numpy as np
import rasterio
import matplotlib.pyplot as plt

def visualize_bands(filename):
    """Let's see what each band looks like"""
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