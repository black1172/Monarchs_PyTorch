import view_data as vd
import load_sattelite_images as lsd

filename = "test\m_3908453_se_16_1_20130924_20131031.jp2"
print(f"Ready to work with: {filename}")
lsd.examine_satellite_data(filename)
