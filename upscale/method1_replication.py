import numpy as np
import cv2

def upscale_replication(cube: np.ndarray, scale: int = 2) -> np.ndarray:

    h, w, bands = cube.shape
    upscaled_cube = np.zeros((h * scale, w * scale, bands), dtype=cube.dtype)

    for b in range(bands):
        upscaled_cube[:, :, b] = cv2.resize(
            cube[:, :, b],
            (w * scale, h * scale),
            interpolation=cv2.INTER_NEAREST
        )

    return upscaled_cube
