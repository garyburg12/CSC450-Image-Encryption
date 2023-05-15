from PIL import Image
from binaryFunctions import *
# Import an image from directory:
# image = Image.open("black2x2.png")

# Extracting pixel map:
# pixel_map_loaded = image.load()

# Extracting the width and height
# of the image:


def blockChain(x, y):
    print("running BlockChain")
    blocks = []
    width, height = x.size
    for i in range(width):
        for j in range(height):
            width, height = x.size
            # getting the RGB pixel value.
            if y==0:
                r, g, b, ozarka = x.getpixel((i, j))
            if y==1:
                r, g, b = x.getpixel((i, j))
            r = convertToBinary(r)
            g = convertToBinary(g)
            b = convertToBinary(b)
            pixel = r + g + b
            blocks.extend(pixel)
    size = len(blocks)//4

    A = blocks[0:size]
    B = blocks[size:size*2]
    C = blocks[size*2:size*3]
    D = blocks[size*3:]
    returnlist = [A, B, C, D]
    return returnlist

# x is a list with the 4 blocks
# imageuse is the image to rebuild to


def rebuild(x, columns, rows):
    print("rebuilding")
    newimage=Image.new(mode="RGB", size=(columns, rows))
    i = 0
    j = 0
    #height, width = imageuse.size
    pixel_map = newimage.load()
    y=x[0] + x[1] + x[2] + x[3]
    for z in range(0, len(y), 24):
            r = y[z:z+8]
            g = y[z+8:z+16]
            b = y[z+16:z+24]

            pixel_map[i, j] = convertToInt(r), convertToInt(g), convertToInt(b)
            j = (j+1) % rows
            if (j == 0):
                i += 1
            if i==columns:
                break
    return newimage

# listed = blockChain(image)
# twobytwo = Image.new(mode="RGB", size=(2, 2))
# rebuild(listed, twobytwo)

# Saving the final output

# as "grayscale.png":
# image.save("new2x2.png")
