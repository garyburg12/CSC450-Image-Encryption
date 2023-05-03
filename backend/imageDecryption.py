from PIL import Image
from binaryFunctions import *
from keyExpansion import *
# Import an image from directory:
image = Image.open("grayscale.png")

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
    a = d
    d = c
    c = b
    d = c
    u = lRotate(binmult(d, (binadd(2 * d, 1))), math.log2(w))
    t = lRotate(binmult(b, (binadd(2 * b, 1))), math.log2(w))
    c = binxor(rRotate(binsub(c, s[2 * i + 1]), t), u)
    a = binxor(rRotate(binsub(a, s[2 * i]), t), t)
d = binsub(d, s[1])
b = binsub(b, s[0])


imageRebuild()
