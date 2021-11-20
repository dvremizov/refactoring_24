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

    def color_pixels(self, currentI, currentJ, medium_brightness):
        for x in range(currentI, currentI + self.size):
            for y in range(currentJ, currentJ + self.size):
                for channel in range(3):
                    self.pixels[x][y][channel] = medium_brightness // self.step * self.step // 3;

    def get_medium_brightness(self, currentI, currentJ):
        sumRgb = 0;
        for x in range(currentI, currentI + self.size):
            for y in range(currentJ, currentJ + self.size):
                pixel = self.pixels[x][y];
                sumRgb += sum(pixel);

        return int(sumRgb // (self.size ** 2));


img = Image.open("img2.jpg")
pixels = np.array(img)
result = Mozabrick(pixels, 10, 50).image_processing();
result.save('res.jpg')