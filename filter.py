import sys

from PIL import Image
import numpy as np


class Mosaica:

    def __init__(self, mosaic_size, mosaic_gradation):
        try:
            self.image = Image.open(input())
        except FileNotFoundError:
            print('Ошибка: несуществующее имя')
            sys.exit()
        self.img_array = np.array(self.image)
        self.img_height = len(self.img_array)
        self.img_width = len(self.img_array[1])
        self.mosaic_size = mosaic_size
        self.gradation = mosaic_gradation

    def mosaic(self, ):
        for height in range(0, self.img_height, self.mosaic_size):
            for width in range(0, self.img_width, self.mosaic_size):
                avg_brightness = self.get_brightness(height, width)
                self.modify_img_array(avg_brightness, height, width, self.mosaic_size, self.gradation)

        res = Image.fromarray(self.img_array)
        return res

    def get_brightness(self, height, width):
        avg_brightness = self.img_array[height: height + self.mosaic_size, width:width + self.mosaic_size].sum()
        return int(avg_brightness // self.mosaic_size ** 2)

    def modify_img_array(self, avg_brightness, height, width, mosaic_modifier, mosaic_step):
        self.img_array[height: height + mosaic_modifier, width:width + mosaic_modifier] = int(
            (avg_brightness // mosaic_step) * mosaic_step) / 3


result = Mosaica(10, 50).mosaic()
result.save('res.jpg')
