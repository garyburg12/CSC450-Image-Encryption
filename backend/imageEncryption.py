# from PIL import Image
from PIL import *
from binaryFunctions import *
from keyExpansion import *
from imageConversion import *
# Import an image from directory:
image = Image.open("grayscale.png")

blockchain = blockChain(image)

a = blockchain[0]
b = blockchain[1]
c = blockchain[2]
d = blockchain[3]


# start encryption
b = binadd(b, s[0])
d = binadd(d, s[1])
i = 1
for i in range(i, r):
    # t = (B x (2 * B + 1)) <<< log(w)
    t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
                convertToBinary(1))), int(math.log2(w)))

    # u = (D X (2 * D + 1)) <<< log(w)
    u = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
                convertToBinary(1))), int(math.log2(w)))

    # A = ((A ^ t) <<< u) + S[2 * i]
    a = binadd(lRotate(binxor(a, t), u), s[2 * i])

    # C = ((C ^ u) <<< t) + S[2 * i + 1]
    c = binadd(lRotate(binxor(c, u), t), s[2 * i + 1])
    a = b
    b = c
    c = d
    d = a
a = binadd(a, s[t - 2])
c = binadd(c, s[t - 1])

# in the xor (a, t) a is longer than t and its causing error
#########################################################################
b = binadd(b, s[0])
d = binadd(d, s[1])
i = 1
for i in range(i, r):
    t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
                convertToBinary(1))), math.log2(w))
    t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
                convertToBinary(1))), math.log2(w))
    a = binadd(lRotate(binxor(a, t), u), s[2 * i])
    c = binadd(lRotate(binxor(c, u), t), s[2 * i + 1])
    a = b
    b = c
    c = d
    d = a
a = binadd(a, s[t - 2])
c = binadd(c, s[t - 1])
###########################################################################


encryptedChain = [a, b, c, d]

# create a new image
im = Image.new(mode="RGB", size=(4, 4))

rebuild(encryptedChain, im)

im.save("encryptedImage.png")
