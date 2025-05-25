import os
import scipy.io
import h5py
import numpy as np

from combine.combine_channels import combine_bands
from downscale.downscale_python import downscale_cube
from upscale.method1_replication import upscale_replication
from upscale.method2_average_interpolation import upscale_average_interpolation


def get_main_variable(mat_contents):
    for key in mat_contents:
        if not key.startswith("__"):
            return key, mat_contents[key]
    raise ValueError("No usable variable found in the .mat file.")

def load_mat_file(path):
    try:
        
        data = scipy.io.loadmat(path)
        var_name, array = get_main_variable(data)
        return var_name, array
    except NotImplementedError:
        
        with h5py.File(path, 'r') as f:
            for key in f.keys():
                dataset = f[key]
                array = dataset[:]
                array = np.transpose(array, (2, 1, 0))  # (bands, width, height) → (H, W, bands)
                return key, array
    except Exception as e:
        raise RuntimeError(f"Failed to load .mat file: {e}")

def main():
    print("Spectral Image Processing Tool")

    mat_path = input("\nEnter the absolute path to the .mat file: ").strip()
    if not os.path.isfile(mat_path):
        print("Error: File does not exist.")
        return

    try:
        var_name, data = load_mat_file(mat_path)
    except Exception as e:
        print(f"Failed to load .mat file: {e}")
        return

    print(f"\nLoaded variable '{var_name}' with shape {data.shape}")

    print("\nChoose an operation:")
    print("1 - Downscale (bicubic, scale=0.5)")
    print("2 - Upscale (method 1: replication, scale=2)")
    print("3 - Upscale (method 2: average interpolation)")
    print("4 - Combine Bands")
    
    op_choice = input("Enter the number of your choice: ").strip()

    try:
        if op_choice == '1':
            result = downscale_cube(data, scale=0.5)
            out_file = 'downscaled.mat'
        elif op_choice == '2':
            result = upscale_replication(data, scale=2)
            out_file = 'upscaled_method1.mat'
        elif op_choice == '3':
            result = upscale_average_interpolation(data)
            out_file = 'upscaled_method2.mat'
        elif op_choice == '4':
            result = combine_bands(data, var_name)
            out_file = 'combined_bands.mat'
        else:
            print("Invalid option.")
            return
    except Exception as e:
        print(f"Error during processing: {e}")
        return

    output_path = os.path.join(os.path.dirname(mat_path), out_file)
    scipy.io.savemat(output_path, {f"{var_name}_processed": result})

    print(f"\n✅ Process completed.")
    print(f"Saved result to: {output_path}")
    print(f"Result shape: {result.shape}")

if __name__ == "__main__":
    main()
