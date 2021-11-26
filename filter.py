from PIL import Image
import numpy as np


def pixel_art(img, mosaic_size, step):
    arr = np.array(img)
    img_height = len(arr)
    img_width = len(arr[1])
    height = 0

    while height < img_height - 1:
        width = 0
        while width < img_width - 1:
            shade = give_shade(arr, mosaic_size, height, width)
            gav(arr, shade, mosaic_size, step, height, width)
            width = width + 10
        height = height + 10
    res = Image.fromarray(arr)
    res.save('res.jpg')


def give_shade(arr, mosaic_size, height, width):
    shade = 0
    for x in range(height, height + mosaic_size):
        for y in range(width, width + mosaic_size):
            shade += int(arr[x][y][0] // 3) + int(arr[x][y][1] // 3) + int(arr[x][y][2] // 3)
    return int(shade // mosaic_size ** 2)


def gav(arr, shade, mosaic_size, step, height, width):
    for n in range(height, height + mosaic_size):
        for n_1 in range(width, width + mosaic_size):
            arr[n][n_1][0] = int(shade // step) * step
            arr[n][n_1][1] = int(shade // step) * step
            arr[n][n_1][2] = int(shade // step) * step


pixel_art(Image.open("img2.jpg"), 10, 50)

