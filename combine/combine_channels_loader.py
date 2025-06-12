import os
import numpy as np
import h5py
import scipy.io as sio
from pathlib import Path

def combine_bands(data: np.ndarray) -> np.ndarray:
    if data.ndim != 3:
        raise ValueError("Expected a 3D array of shape (H, W, Bands)")
    
    H, W, B = data.shape
    new_band_count = B // 2
    combined_cube = np.zeros((H, W, new_band_count), dtype=np.float32)

    for i in range(new_band_count):
        combined_cube[:, :, i] = (data[:, :, 2 * i] + data[:, :, 2 * i + 1]) / 2

    if B % 2 == 1:
        combined_cube = np.concatenate((combined_cube, data[:, :, -1][:, :, np.newaxis]), axis=2)

    return combined_cube

def load_v73_mat(filepath, key="cube"):
    with h5py.File(filepath, 'r') as f:
        data = np.array(f[key])  # shape: (Bands, W, H) usually
        data = np.transpose(data, (2, 1, 0))  # to (H, W, Bands)
        return data.astype(np.float32)

def process_folder(input_dir, output_dir, key_name='cube'):
    os.makedirs(output_dir, exist_ok=True)

    mat_files = sorted(Path(input_dir).glob("*.mat"))
    print(f"Found {len(mat_files)} files in {input_dir}")

    for file_path in mat_files:
        print(f"Processing {file_path.name}...", end=" ")

        try:
            cube = load_v73_mat(str(file_path), key=key_name)
        except Exception as e:
            print(f"Error reading {file_path.name}: {e}")
            continue

        try:
            combined = combine_bands(cube)
        except Exception as e:
            print(f"Error combining bands in {file_path.name}: {e}")
            continue

        out_file = Path(output_dir) / file_path.name
        sio.savemat(out_file, {key_name: combined})
        print("Done")

# ==== Set paths ====
input_folder = "./"
output_folder = "../"

process_folder(input_folder, output_folder)
