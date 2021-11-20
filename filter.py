from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
height = 0
while height < a:
    width = 0
    while width < a1:
        s = 0
        for n in range(height, height + 10):
            for n0 in range(width, width + 10):
                n1 = arr[n][n0][0]
                n2 = arr[n][n0][1]
                n3 = arr[n][n0][2]
                M = int(n1) + int(n2) + int(n3)
                s += M
        s = int(s // 100)
        for n in range(height, height + 10):
            for n0 in range(width, width + 10):
                arr[n][n0][0] = int((s // 50) * 50)/3
                arr[n][n0][1] = int((s // 50) * 50)/3
                arr[n][n0][2] = int((s // 50) * 50)/3
        width = width + 10
    height = height + 10
res = Image.fromarray(arr)
res.save('res.jpg')
