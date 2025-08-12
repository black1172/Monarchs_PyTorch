import requests
import os
import numpy as np
import rasterio

def debug_file(filename):
    print(f"\n🔧 Debugging {filename}...")
    
    if os.path.exists(filename):
        file_size = os.path.getsize(filename)
        print(f"File size: {file_size} bytes")
        
        # Read first few bytes to see what we actually got
        with open(filename, 'rb') as f:
            first_bytes = f.read(100)
            print(f"First 100 bytes: {first_bytes}")
            
        # Also read as text to see if it's an HTML error
        with open(filename, 'r', errors='ignore') as f:
            first_text = f.read(200)
            print(f"As text: {first_text}")
    else:
        print("File doesn't exist!")

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