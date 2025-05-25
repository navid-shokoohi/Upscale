import numpy as np

def combine_bands(data: np.ndarray, name: str = "") -> np.ndarray:

    if data.ndim != 3:
        raise ValueError("Expected a 3D array of shape (H, W, Bands)")

    H, W, B = data.shape
    new_band_count = B // 2
    combined_cube = np.zeros((H, W, new_band_count), dtype=data.dtype)

    for i in range(new_band_count):
        combined_cube[:, :, i] = (data[:, :, 2*i] + data[:, :, 2*i + 1]) / 2

    # If number of bands is odd, append the last band
    if B % 2 == 1:
        combined_cube = np.concatenate((combined_cube, data[:, :, -1][:, :, np.newaxis]), axis=2)

    return combined_cube
