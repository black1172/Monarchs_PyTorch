import requests
import os
import numpy as np
import rasterio

def download_sample():
    # This is a small Sentinel-2 sample file
    url = "https://github.com/mommermi/geotiff_sample/raw/master/sample.tif"
    filename = "sample_satellite.tif"
    
    if not os.path.exists(filename):
        print("Downloading sample file...")

        # Step 1: Make a request to get the file
        response = requests.get(url)
        
        # Step 2: Save the content to a file
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"Downloaded {filename}")
    else:
        print("Sample file already exists!")
    return filename

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
    filename = download_sample()
    print(f"Ready to work with: {filename}")
    examine_satellite_data(filename)