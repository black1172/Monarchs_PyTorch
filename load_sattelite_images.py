import requests
import os

def download_sample():
    # This is a small Sentinel-2 sample file
    url = "https://github.com/sentinel-hub/eo-learn/raw/master/example_data/TestEOPatch/data_timeless/DEM/DEM.tif"
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

# TEST CODE
if __name__ == "__main__":
    filename = download_sample()
    print(f"Ready to work with: {filename}")