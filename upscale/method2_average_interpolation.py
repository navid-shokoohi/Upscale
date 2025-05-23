import numpy as np
from scipy.io import loadmat, savemat

# Load downscaled cube
mat_data = loadmat('sample_downscale.mat')
downscaled_cube = mat_data['downscaled_cube']

def upsample_average_2x(image):
    h, w = image.shape

    # Pad if odd dimensions
    if h % 2 != 0:
        image = np.vstack((image, image[-1:, :]))
        h += 1
    if w % 2 != 0:
        image = np.hstack((image, image[:, -1:]))
        w += 1

    up = np.zeros((h * 2, w * 2), dtype=np.float32)

    # Place original pixels
    up[::2, ::2] = image

    # Horizontal interpolation
    up[::2, 1:-1:2] = (image[:, :-1] + image[:, 1:]) / 2
    up[::2, -1] = image[:, -1]

    # Vertical interpolation
    up[1:-1:2, ::2] = (image[:-1, :] + image[1:, :]) / 2
    up[-1, ::2] = image[-1, :]

    # Diagonal interpolation
    up[1:-1:2, 1:-1:2] = (
        image[:-1, :-1] + image[:-1, 1:] +
        image[1:, :-1] + image[1:, 1:]
    ) / 4
    up[-1, -1] = image[-1, -1]

    return up

# Upsample each band and collect them
upsampled_bands = []
for b in range(downscaled_cube.shape[2]):
    up_band = upsample_average_2x(downscaled_cube[:, :, b].astype(np.float32))
    upsampled_bands.append(up_band)

# Stack along third axis
upscaled_cube2 = np.stack(upsampled_bands, axis=2)

# Save the result
savemat('sample_upscaled_method2.mat', {'upscaled_cube2': upscaled_cube2})
print(f"Upcaled: {upscaled_cube2.shape}")
print("Upscaled using method 2 (average interpolation).")