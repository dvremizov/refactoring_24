from PIL import Image
import numpy as np


def image_to_mosaic(source_img, size, grayscale_step_count):
    grayscale_step = 255 / grayscale_step_count
    source_arr = np.array(source_img)
    width, height, _ = source_arr.shape
    for i in range(0, width, size):
        for j in range(0, height, size):
            s = np.mean(source_arr[i:i + size, j:j + size], dtype=np.int32)
            color = s // grayscale_step * grayscale_step
            source_arr[i:i + size, j:j + size] = color
    res = Image.fromarray(source_arr)
    res.save('images/res.jpg')


if __name__ == '__main__':
    img = Image.open('images/img2.jpg')
    image_to_mosaic(img, 10, 5)
