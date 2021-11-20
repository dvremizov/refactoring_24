from PIL import Image
import numpy as np

GRAYSCALE_STEP_COUNT = 4
GRAYSCALE_STEP = 255 / GRAYSCALE_STEP_COUNT
SIZE = 5


def calc_average(arr, x, y):
    s = 0
    for n in range(x, x + SIZE):
        for k in range(y, y + SIZE):
            r = arr[n][k][0]
            g = arr[n][k][1]
            b = arr[n][k][2]
            s += int(r) + int(g) + int(b)
    return int(s // SIZE ** 2)


def calc_grayscale(arr, x, y, color):
    for n in range(x, x + SIZE):
        for k in range(y, y + SIZE):
            arr[n][k][0] = color
            arr[n][k][1] = color
            arr[n][k][2] = color


def main():
    source_img = Image.open('img2.jpg')
    source_arr = np.array(source_img)
    for i in range(0, len(source_arr), SIZE):
        for j in range(0, len(source_arr[1]), SIZE):
            s = calc_average(source_arr, i, j)
            color = int(s // GRAYSCALE_STEP) * GRAYSCALE_STEP // 3
            calc_grayscale(source_arr, i, j, color)
    res = Image.fromarray(source_arr)
    res.save('res.jpg')


if __name__ == '__main__':
    main()
