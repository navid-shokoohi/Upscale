import numpy as np
import cv2
import os
from scipy.io import loadmat, savemat

# Define your source and destination folder paths here:
SOURCE_FOLDER = '../../Dataset16'
DESTINATION_FOLDER = '../../Dataset16_DS'

def downscale_cube(cube: np.ndarray, scale: float = 0.5) -> np.ndarray:
    height, width, bands = cube.shape
    new_h = int(height * scale)
    new_w = int(width * scale)
    downscaled_cube = np.zeros((new_h, new_w, bands), dtype=cube.dtype)
    for b in range(bands):
        downscaled_cube[:, :, b] = cv2.resize(
            cube[:, :, b],
            (new_w, new_h),
            interpolation=cv2.INTER_CUBIC
        )
    return downscaled_cube

def batch_downscale(src_folder: str, dst_folder: str, scale: float = 0.5):
    os.makedirs(dst_folder, exist_ok=True)
    
    for filename in os.listdir(src_folder):
        if filename.lower().endswith('.mat'):
            filepath = os.path.join(src_folder, filename)
            print(f"Processing {filename}...")

            # Load the .mat file
            data = loadmat(filepath)
            cube_data = data['cube']

            # Downscale the cube
            downscaled = downscale_cube(cube_data, scale)

            # Save the downscaled cube back into a new .mat file
            save_path = os.path.join(dst_folder, filename)
            savemat(save_path, {'cube': downscaled})

            print(f"Saved downscaled cube to {save_path}")

if __name__ == "__main__":
    batch_downscale(SOURCE_FOLDER, DESTINATION_FOLDER, scale=0.5)

