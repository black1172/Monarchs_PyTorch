import view_data as vd
import load_sattelite_images as lsd
import matplotlib.pyplot as plt
import rasterio
import model

filename = "test\m_3908453_se_16_1_20130924_20131031.jp2"
print(f"Ready to work with: {filename}")
satellite_tensor = lsd.load_satellite_image_as_tensor(filename)
vd.test_patch(satellite_tensor)
