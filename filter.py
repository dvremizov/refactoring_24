from PIL import Image
import numpy as np


def mosaic(image, mosaic_modifier, mosaic_step):
    img_arr = np.array(image)
    img_height = len(img_arr)
    img_width = len(img_arr[1])
    height = 0

    while height < img_height:
        width = 0
        while width < img_width:
            avg_brightness = get_brightness(img_arr, height, width, mosaic_modifier)
            modify_img_array(img_arr, avg_brightness, height, width, mosaic_modifier, mosaic_step)
            width = width + mosaic_modifier
        height = height + mosaic_modifier
    res = Image.fromarray(img_arr)
    res.save('res.jpg')


def get_brightness(image_array, height, width, modifier):
    brightness = 0
    for y in range(height, height + modifier):
        for x in range(width, width + modifier):
            brightness += int(image_array[y][x][0]) + int(image_array[y][x][1]) + int(image_array[y][x][2])
    return int(brightness // modifier ** 2)


def modify_img_array(img_arr, avg_brightness, height, width, mosaic_modifier, mosaic_step):
    for y in range(height, height + mosaic_modifier):
        for x in range(width, width + mosaic_modifier):
            img_arr[y][x][0] = int((avg_brightness // mosaic_step) * mosaic_step) / 3
            img_arr[y][x][1] = int((avg_brightness // mosaic_step) * mosaic_step) / 3
            img_arr[y][x][2] = int((avg_brightness // mosaic_step) * mosaic_step) / 3


mosaic(Image.open("img2.jpg"), 10, 50)
