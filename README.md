# 🧪 Simple Spectral Image Processing Toolkit

This repository provides simple Python and MATLAB methods for preprocessing spectral (hyperspectral) images. These methods include downscaling, upscaling, and spectral band combination. The goal is to provide lightweight baseline techniques for comparison in tasks like image super-resolution, especially when evaluating diffusion models.

---

## 📁 Contents

### 🔧 Main Script (Python CLI)

- `main.py`:  
  Command-line interface for processing `.mat` spectral cubes.  
  Offers:
  - Downscaling (bicubic)
  - Upscaling (replication or average interpolation)
  - Band combination (e.g., from 31 bands to 16)  
  Output is saved in the same folder as the input.

---

### 🔼 Upscaling Methods (Python)

- `upscale/method1_replication.py`:  
  Upscales a spectral cube by repeating pixels (nearest-neighbor interpolation).  
  Output: `upscaled_method1.mat`

- `upscale/method2_average_interpolation.py`:  
  Upscales using average-based interpolation of neighbors.  
  Output: `upscaled_method2.mat`

---

### 🔽 Downscaling Methods

- `downscale/downscale_matlab.m`:  
  MATLAB script that downsamples a spectral cube using bicubic interpolation.  
  Output: `sample_downscaled_mat.mat`

- `downscale/downscale_python.py`:  
  Python version using OpenCV for bicubic downsampling.  
  Output: `downscaled.mat`

---

### 🎨 Band Combination

- `combine/combine_channels.py`:  
  Reduces a spectral cube from 31 to 16 bands by averaging adjacent channels.  
  Output: `combined_bands.mat`

---

## 🧪 Sample Data Format

You should provide your own `.mat` file containing a 3D variable (spectral cube):

- Shape: `(height, width, bands)`
- Example variable name: `cube`

Supports both old-style (`.mat` v7) and newer HDF5-based (`.mat` v7.3) files.

---

## ⚙️ Requirements

### Python

Install dependencies via pip:

```bash
pip install numpy scipy h5py opencv-python
