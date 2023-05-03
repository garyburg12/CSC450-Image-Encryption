from PIL import Image
x = Image.open("encryptedImage.png")

pixel_map = x.load()

for i in range(4):
    for j in range(4):
        a, b, c = x.getpixel((i, j))
        print(a, b, c)
        # if abs((i-2)*(j-2)) == 1:
        # if 0 < i and i < 3 and 0 < j and j < 3:
        #    pixel_map[i, j] = (255, 255, 255)
        # pixel_map[i, j] = (0, 0, 0)
# x.save("circle.png")
