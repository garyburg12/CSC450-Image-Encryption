from PIL import Image
from binaryFunctions import *
# x = Image.open("inversecircle.png")

# pixel_map = x.load()

# for i in range(4):
#    for j in range(4):
#        a, b, c = x.getpixel((i, j))
#        # if abs((i-2)*(j-2)) == 1:
#        if 0 < i and i < 3 and 0 < j and j < 3:
#            # pixel_map[i, j] = (255, 255, 255)
#            pixel_map[i, j] = (0, 0, 0)
#        # pixel_map[i, j] = (0, 0, 0)
#        # pixel_map[i, j] = (255, 255, 255)
# x.save("inversecircle.png")

# twobytwo = Image.new(mode="RGB", size=(50, 50), color=(0, 0, 0))

# twobytwo.save("black50x50.jpg")
b = 6

something = [3, 5, 4, 5, 7, 1]
# for i in range(0, b):
#    something[i] = convertToBinary(something[i])

# y = 3
# y = y % len(something)
# for i in range(0, y):
#    something = something[1:]+[something[0]]
# print(something)

lRotate(something, 3)
print(something)
# rRotate(something, 2)
# print(something)
