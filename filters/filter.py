import numpy as np
from PIL import Image

def generate_pixel_art(input_file, mosaic_size, grayscale):
    img = Image.open(input_file)
    arr = np.array(img)
    height = len(arr)
    width = len(arr[1])

    for i in range(0, height, mosaic_size):
        for j in range(0, width, mosaic_size):
            pixel = arr[i: i + mosaic_size, j: j + mosaic_size].sum() / 3
            pixel = pixel // (100 * grayscale) * grayscale
            arr[i: i + mosaic_size, j: j + mosaic_size] = pixel

    return Image.fromarray(arr)


