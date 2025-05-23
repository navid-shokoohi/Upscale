# Method 2: Insert-Zero-Then-Average (Linear Style Interpolation)
import numpy as np
import cv2
from scipy.io import loadmat, savemat

def upsample_average_2x(image):
    h, w = image.shape
    up = np.zeros((h * 2, w * 2), dtype=np.float32)

    # Place original pixels
    up[::2, ::2] = image

    # Horizontal interpolation
    up[::2, 1::2] = (image[:, :-1] + image[:, 1:]) / 2

    # Vertical interpolation
    up[1::2, ::2] = (image[:-1, :] + image[1:, :]) / 2

    # Diagonal interpolation
    up[1::2, 1::2] = (image[:-1, :-1] + image[:-1, 1:] + image[1:, :-1] + image[1:, 1:]) / 4

    return up

# Apply this for each band
upscaled_cube2 = np.zeros((downscaled_cube.shape[0]*2, downscaled_cube.shape[1]*2, downscaled_cube.shape[2]), dtype=np.float32)

for b in range(downscaled_cube.shape[2]):
    upscaled_cube2[:, :, b] = upsample_average_2x(downscaled_cube[:, :, b].astype(np.float32))

savemat('ARAD_1K_0912_upscaled_method2.mat', {'upscaled_cube2': upscaled_cube2})
print("Upscaled using method 2 (average interpolation).")
