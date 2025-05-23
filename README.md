# Simple Upscaling Methods for Spectral Image Comparison

This repository contains two simple Python methods for image upscaling. These are used as baseline comparison methods in the context of evaluating super-resolution performance of diffusion models applied to spectral image data.

---

## 📋 Contents

- `method_1_repeat_and_scale.py`: Upscaling by pixel repetition (reverse of downscaling ratio)
- `method_2_insert_and_average.py`: Upscaling by inserting empty pixels and averaging neighbors
- `example_input.mat`: Example input image (you must provide your own `.mat` file with a 3D array `cube`)
- `README.md`: This file

---

## ⚙️ Requirements

- Python 3.7–3.10 (via Conda recommended)
- Required libraries:
  ```bash
  pip install numpy scipy h5py opencv-python
