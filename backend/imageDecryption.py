from PIL import Image
from binaryFunctions import *
from keyExpansion import *
from imageConversion import *
# Import an image from directory:
image = Image.open("encryptedImage.png")

blockchain = blockChain(image)

a = blockchain[0]
b = blockchain[1]
c = blockchain[2]
d = blockchain[3]


# start encryption

c = binsub(c, s[m - 1])
a = binsub(a, s[m - 2])
i = r
for i in range(r, 1):
    temp = d
    d = c
    c = b
    b = a
    a = temp

    # u = (D X (2 * D + 1)) <<< log(w)
    u = lRotate(multmod2(d, binadd(binmult(convertToBinary(2), d),
                convertToBinary(1))), int(math.log2(w)))

    # t = (B x (2 * B + 1)) <<< log(w)
    t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
                convertToBinary(1))), int(math.log2(w)))

    # C = ((C - S[2 * i + 1]) >>> t) ^ u
    c = binxor(rRotate(binsub(c, s[2 * i + 1]), convertToInt(t)), u)

    # A = ((A - S[2 * i]) >>> u) ^ t
    a = binxor(rRotate(binsub(a, s[2 * i]), convertToInt(u)), t)

d = binsub(d, s[1])
b = binsub(b, s[0])


decryptedChain = [a, b, c, d]

# create a new image
im = Image.new(mode="RGB", size=(4, 4))

rebuild(decryptedChain, im)

im.save("decryptedImage.png")
