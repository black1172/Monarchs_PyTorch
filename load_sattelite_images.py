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


def download_sample():
    import requests

    # Correct raw GitHub link
    url = "https://raw.githubusercontent.com/mommermi/geotiff_sample/master/sample.tif"
    filename = "sample_satellite.tif"

    if os.path.exists(filename):
        print("Sample file already exists!")
        return filename

    print("Downloading sample file...")

    # Step 1: Make a request with streaming
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Stop if HTTP error

    # Step 2: Save file in chunks
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    # Step 3: Validate file magic number (TIFF starts with 'II' or 'MM')
    with open(filename, 'rb') as f:
        start_bytes = f.read(4)
        if not (start_bytes.startswith(b'II') or start_bytes.startswith(b'MM')):
            os.remove(filename)
            raise ValueError("Downloaded file is not a valid TIFF. It may be HTML or an error page.")

    print(f"Downloaded and verified: {filename}")
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
    debug_file(filename)
    examine_satellite_data(filename)