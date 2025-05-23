# Method 1: Replicate (Nearest Neighbor-style) Upsampling
import numpy as np
import cv2
from scipy.io import loadmat, savemat

# Load downscaled cube
mat_data = loadmat('sample_downscale.mat')
downscaled_cube = mat_data['downscaled_cube']

scale = 2  # Reciprocal of 0.5 (used for downscaling)

# Get dimensions
h, w, bands = downscaled_cube.shape
upscaled_cube1 = np.zeros((h * scale, w * scale, bands), dtype=downscaled_cube.dtype)

# Nearest-neighbor-like replication (using INTER_NEAREST)
for b in range(bands):
    upscaled_cube1[:, :, b] = cv2.resize(
        downscaled_cube[:, :, b],
        (w * scale, h * scale),
        interpolation=cv2.INTER_NEAREST
    )

# Save the result
savemat('sample_upscaled_method1.mat', {'upscaled_cube1': upscaled_cube1})
print(f"Upcaled: {upscaled_cube1.shape}")
print("Upscaled using method 1 (replication).")

