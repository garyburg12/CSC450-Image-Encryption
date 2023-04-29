from PIL import Image
from binaryFunctions import *
# Import an image from directory:
image = Image.open("circle.png")
  
# Extracting pixel map:
pixel_map_loaded = image.load()

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
def rebuild(x, imageuse):
    i=0
    j=0
    for y in x:
        for z in range(0, len(y), 24):
             r = y[z:z+8]
             g = y[z+8:z+16]
             b = y[z+16:z+24]
             pixel_map = imageuse.load()
             height, width = imageuse.size
             pixel_map[i, j] = convertToInt(r), convertToInt(g), convertToInt(b)
             i=(i+1) % width
             if(i==0):
                 j+=1
             
    
#listed = blockChain(image)
#rebuild(listed, image)

# Saving the final output

# as "grayscale.png":
image.save("grayscale.png")