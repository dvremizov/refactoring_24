from PIL import Image
import numpy as np
img = Image.open(input("Введите имя исходного изображения: "))
mosaicSize = int(input("Введите размер мозаики: "))
grayscale = int(input("Введите желаемую градацию серого: "))

def getMosaicImg(img, mosaicSize, grayscale):
    arr = np.array(img)
    height, width = len(arr), len(arr[1])
    for i in range(0, height, mosaicSize):
        for j in range(0, width, mosaicSize):
            rgbGrey = arr[i:i + mosaicSize, j:j + mosaicSize].sum() // 100 // 3 // grayscale * grayscale
            arr[i:i + mosaicSize, j:j + mosaicSize] = rgbGrey
    return Image.fromarray(arr)

getMosaicImg(img, mosaicSize, grayscale).save(input("Введите имя результирующего изображения: "))
