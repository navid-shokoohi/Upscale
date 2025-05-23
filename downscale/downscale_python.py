import numpy as np
import h5py
import cv2
from scipy.io import savemat

# Load the .mat file (v7.3 format)
with h5py.File('sample.mat', 'r') as f:
    cube = f['cube'][:]
    cube = np.transpose(cube, (2, 1, 0))  # (height, width, bands)

# Define scale factor
scale = 0.5

# Get original size
height, width, bands = cube.shape

# Preallocate
downscaled_cube = np.zeros((int(height * scale), int(width * scale), bands), dtype=cube.dtype)

for b in range(bands):
    downscaled_cube[:, :, b] = cv2.resize(
        cube[:, :, b],
        (int(width * scale), int(height * scale)),
        interpolation=cv2.INTER_CUBIC
    )

savemat('sample_downscale.mat', {'downscaled_cube': downscaled_cube})

print(f"Downscaled: {downscaled_cube.shape}")
