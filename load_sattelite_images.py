import requests
import os
import numpy as np
import rasterio
import torch

def load_satellite_image_as_tensor(filename):
    with rasterio.open(filename) as src:
        data = src.read().astype(float)
        # Convert to PyTorch tensor
        tensor = torch.from_numpy(data)
        return tensor