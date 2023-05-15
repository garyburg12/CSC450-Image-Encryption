import math
from binaryFunctions import *
from PIL import Image
# key length
#b = 8

# secret key
k = [11234, 356, 8765, 845, 3356, 476, 4873, 2345]
image=Image.open("white.png")
# convert ints to binary
pixelmap=image.load()
pixelmap[0, 1]= 0, 255, 0
#for i in range(0, b):
#    k[i] = convertToBinary(k[i])
image.save("white.png")
# print(k)
for i in k:
    i=convertToBinary(i)
    print(i)
    print(convertToInt(i))