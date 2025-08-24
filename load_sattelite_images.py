import requests
import os
import numpy as np
import rasterio
import torch

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

def load_satellite_image_as_tensor(filename):
    with rasterio.open(filename) as src:
        data = src.read().astype(float)
        # Convert to PyTorch tensor
        tensor = torch.from_numpy(data)
        return tensor