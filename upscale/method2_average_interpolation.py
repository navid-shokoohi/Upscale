import numpy as np

def upsample_average_2x(image: np.ndarray) -> np.ndarray:

    h, w = image.shape

    if h % 2 != 0:
        image = np.vstack((image, image[-1:, :]))
        h += 1
    if w % 2 != 0:
        image = np.hstack((image, image[:, -1:]))
        w += 1

    up = np.zeros((h * 2, w * 2), dtype=np.float32)

    up[::2, ::2] = image
    up[::2, 1:-1:2] = (image[:, :-1] + image[:, 1:]) / 2
    up[::2, -1] = image[:, -1]
    up[1:-1:2, ::2] = (image[:-1, :] + image[1:, :]) / 2
    up[-1, ::2] = image[-1, :]
    up[1:-1:2, 1:-1:2] = (
        image[:-1, :-1] + image[:-1, 1:] +
        image[1:, :-1] + image[1:, 1:]
    ) / 4
    up[-1, -1] = image[-1, -1]

    return up

def upscale_average_interpolation(cube: np.ndarray) -> np.ndarray:

    upscaled_bands = []
    for b in range(cube.shape[2]):
        band = cube[:, :, b].astype(np.float32)
        up_band = upsample_average_2x(band)
        upscaled_bands.append(up_band)

    return np.stack(upscaled_bands, axis=2)
