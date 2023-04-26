from PIL import Image
from binaryFunctions import *
# Import an image from directory:
image = Image.open("grayscale.png")
  
# Extracting pixel map:
pixel_map = image.load()

# Extracting the width and height 
# of the image:

def blockChain(x):
    blocks = []
    width, height = x.size
    print (width)
    print(height)
    for i in range(width):
        for j in range(height):
            width, height = x.size
            # getting the RGB pixel value.
            r, g, b = x.getpixel((i, j))

            r = convertToBinary(r)
            g = convertToBinary(g)
            b = convertToBinary(b)
            pixel = r + g + b
            blocks = blocks + pixel
    size = len(blocks)//4
    A = blocks[0:size]
    B = blocks[size:size*2]
    C = blocks[size*2:size*3]
    D = blocks[size*3:size*4]
    returnlist = [A, B, C, D]
    return returnlist
# Saving the final output
# as "grayscale.png":
image.save("grayscale.png")