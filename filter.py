from PIL import Image
import numpy as np

class Mozabrick:
    def __init__(self, pixels, size, step):
        self.pixels = pixels;
        self.height = len(pixels);
        self.width = len(pixels[1]);
        self.size = size;
        self.step = step;

    def image_processing(self):
        for i in range(0, self.height, self.size):
            for j in range(0, self.width, self.size):
                medium_brightness = self.get_medium_brightness(i, j);
                self.color_pixels(i, j, medium_brightness);
        return Image.fromarray(self.pixels);

    def color_pixels(self, i, j, medium_brightness):
        self.pixels[i : i + self.size, j : j + self.size] = medium_brightness // self.step * self.step // 3;

    def get_medium_brightness(self, i, j):
        sumRgb = self.pixels[i : i + self.size, j : j + self.size].sum();
        return int(sumRgb // (self.size ** 2));


inputImg = Image.open(input("Введите полный путь обрабатываемого изображения: "));
outputNameImg = input("Введите имя нового изображения: ");
pixels = np.array(inputImg);
result = Mozabrick(pixels, 10, 50).image_processing();
result.save(outputNameImg);