import numpy as np
from PIL import Image

def generate_pixel_art(mosaic_size = 10, grayscale = 50):
    img = Image.open("img/origin.jpg")
    arr = np.array(img)
    height = len(arr)
    width = len(arr[1])

    for i in range(0, height, mosaic_size):
        for j in range(0, width, mosaic_size):
            pixel = arr[i: i + mosaic_size, j: j + mosaic_size].sum() / 3
            pixel = pixel // (100 * grayscale) * grayscale
            arr[i: i + mosaic_size, j: j + mosaic_size] = pixel

    res = Image.fromarray(arr)
    res.save("img/res2.jpg")