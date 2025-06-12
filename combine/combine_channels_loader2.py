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

def find_first_3d_array(mat_dict):
    """Find the first key in mat_dict whose value is a 3D numpy array."""
    for key, val in mat_dict.items():
        if isinstance(val, np.ndarray) and val.ndim == 3:
            return key, val
    raise KeyError("No 3D ndarray found in the .mat file")

def load_mat_file(filepath):
    """Load .mat file (v7.3 or earlier), return the first 3D array found."""
    try:
        with h5py.File(filepath, 'r') as f:
            # Find first 3D dataset in HDF5 file
            def visitor(name, obj):
                if isinstance(obj, h5py.Dataset):
                    if len(obj.shape) == 3:
                        visitor.found = (name, np.array(obj))
            visitor.found = None
            f.visititems(visitor)
            if visitor.found is None:
                raise KeyError("No 3D dataset found in the HDF5 .mat file")
            key, data = visitor.found
            data = np.transpose(data, (2, 1, 0))  # Adjust dimension order
            return data.astype(np.float32)
    except (OSError, KeyError):
        # Load older format .mat file with scipy.io
        mat_contents = sio.loadmat(filepath)
        key, data = find_first_3d_array(mat_contents)
        return data.astype(np.float32)

def process_folder(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    mat_files = sorted(Path(input_dir).glob("*.mat"))
    print(f"Found {len(mat_files)} files in {input_dir}")

    for file_path in mat_files:
        print(f"Processing {file_path.name}...", end=" ")

        try:
            cube = load_mat_file(str(file_path))
        except Exception as e:
            print(f"Error reading {file_path.name}: {e}")
            continue

        try:
            combined = combine_bands(cube)
        except Exception as e:
            print(f"Error combining bands in {file_path.name}: {e}")
            continue

        out_file = Path(output_dir) / file_path.name
        sio.savemat(out_file, {"cube": combined})  # Save with fixed key 'cube'
        print("Done")

# ==== Set paths ====
input_folder = r"C:\Users\navid\Git\DataSets\CAVE\31-float32"
output_folder = r"C:\Users\navid\Git\DataSets\CAVE\16-float32"

process_folder(input_folder, output_folder)
