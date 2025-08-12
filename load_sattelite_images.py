import requests
import os
import numpy as np
import rasterio

def examine_satellite_data(filename):
    print(f"\nExamining {filename}...")
    
    # Open the satellite file
    with rasterio.open(filename) as src:
        data = src.read()  # This reads all the bands
        
        print(f"Data shape: {data.shape}")
        print(f"Data type: {data.dtype}")
        print(f"Min value: {data.min()}")
        print(f"Max value: {data.max()}")

# TEST CODE
if __name__ == "__main__":
    filename = "test\m_3908453_se_16_1_20130924_20131031.jp2"
    print(f"Ready to work with: {filename}")
    debug_file(filename)
    examine_satellite_data(filename)