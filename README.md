# Simple Spectral Image Processing Toolkit

This repository provides simple Python and MATLAB methods for preprocessing spectral (hyperspectral) images. These methods include downscaling, upscaling, and spectral band combination. The goal is to provide lightweight baseline techniques for comparison in tasks like image super-resolution, especially when evaluating diffusion models.

---

## 📁 Contents

### 🔼 Upscaling Methods (Python)

- `method_1_repeat_and_scale.py`:  
  Upscales a spectral cube by repeating pixels (nearest-neighbor interpolation).  
  Output: `sample_upscaled_method1.mat`

- `method_2_insert_and_average.py`:  
  Upscales using a simple interpolation by inserting and averaging neighbors.  
  Output: `sample_upscaled_method2.mat`

### 🔽 Downscaling Methods

- `downscale_matlab.m`:  
  MATLAB script that downsamples a spectral cube using bicubic interpolation.  
  Output: `sample_downscaled_mat.mat`

- `downscale_python.py`:  
  Python equivalent of the MATLAB downscaling method using OpenCV (bicubic).  
  Output: `sample_downscaled_py.mat`

Both methods return the new dimensions and number of bands after downscaling.

### 🧪 Band Combination

- `combine_31_to_16_bands.py`:  
  Reduces a spectral cube from 31 bands to 16 by averaging adjacent bands.  
  Output: `sample_combined.mat`

---

## 🧪 Sample Data

You should provide your own input `.mat` file with a 3D array named `cube`:
- Dimensions: `(height, width, bands)`
- Example filename: `sample.mat`

---

## ⚙️ Requirements

### Python

- Python 3.7–3.10 (install via [Miniconda](https://docs.conda.io/en/latest/miniconda.html) recommended)
- Required libraries:

```bash
pip install numpy scipy h5py opencv-python
