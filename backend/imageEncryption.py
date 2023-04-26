from PIL import Image
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
    t = lRotate(binmult(b, (binadd(2 * b, 1))), math.log2(w))
    u = lRotate(binmult(d, (binadd(2 * d, 1))), math.log2(w))
    a = binadd(lRotate(binxor(a, t), u), s[2 * i])
    c = binadd(lRotate(binxor(c, u), t), s[2 * i + 1])
    a = b
    b = c
    c = d
    d = a
a = binadd(a, s[t - 2])
c = binadd(c, s[t - 1])

# imageRebuild()
