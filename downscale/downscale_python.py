import numpy as np
import cv2

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
