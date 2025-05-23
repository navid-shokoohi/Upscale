import h5py
import numpy as np
import scipy.io as sio

with h5py.File('sample.mat', 'r') as f:
    cube = f['cube'][:]  # (bands, width, height)
    cube = np.transpose(cube, (2, 1, 0))  # (H, W, bands)

H, W, B = cube.shape
new_band_count = B // 2
combined_cube = np.zeros((H, W, new_band_count), dtype=cube.dtype)

for i in range(new_band_count):
    combined_cube[:, :, i] = (cube[:, :, 2*i] + cube[:, :, 2*i + 1]) / 2

# If B is odd (e.g., 31), append the last band
if B % 2 == 1:
    combined_cube = np.concatenate((combined_cube, cube[:, :, -1][:, :, np.newaxis]), axis=2)

sio.savemat("sample_combined.mat", {'combined_cube': combined_cube})
print(f"Combined to shape: {combined_cube.shape}")
