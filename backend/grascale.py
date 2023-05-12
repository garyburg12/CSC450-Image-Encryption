from PIL import Image
image = Image.open("100x100.png")
pixel_map=image.load()
width, length = image.size
for i in range(width):
    for j in range(length):
        r, g, b = pixel_map[i, j]
        r = int((r + g + b) / 3)
        g = r
        b = r
        pixel_map[i, j]= r, g, b
image.save("grayscale.png")