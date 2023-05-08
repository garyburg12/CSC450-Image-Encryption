# from PIL import Image
from PIL import *
from binaryFunctions import *
from keyExpansion import *
from imageConversion import *
# Import an image from directory:
# image = Image.open("checker.png")
image = Image.open("100x100.png")

print("starting block chain")
blockchain = blockChain(image)

# print("block chain")
# print(blockchain)
a = blockchain[0]
b = blockchain[1]
c = blockchain[2]
d = blockchain[3]


# start encryption
print("starting encryption")
b = binadd(b, s[0])
d = binadd(d, s[1])
i = 1  # we had this at 1 before
for i in range(i, r+1):
    # t = (B x (2 * B + 1)) <<< log(w)
    t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
                convertToBinary(1))), int(math.log2(w)))

    # u = (D X (2 * D + 1)) <<< log(w)
    u = lRotate(multmod2(d, binadd(binmult(convertToBinary(2), d),
                convertToBinary(1))), int(math.log2(w)))
    print(t)
    # A = ((A ^ t) <<< u) + S[2 * i]
    a = binadd(lRotate(binxor(a, t), convertToInt(u)), s[2 * i])
    # changed u to convertToInt(u) and changed t in the one below

    # C = ((C ^ u) <<< t) + S[2 * i + 1]
    c = binadd(lRotate(binxor(c, u), convertToInt(t)), s[(2 * i) + 1])

    temp = a

    a = b
    b = c
    c = d
    d = temp
a = binadd(a, s[m - 2])
c = binadd(c, s[m - 1])

# changed both of these to converttoint(t) istead of t
# in the xor (a, t) a is longer than t and its causing error
#########################################################################
# b = binadd(b, s[0])
# d = binadd(d, s[1])
# i = 1
# for i in range(i, r):
#    t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
#                convertToBinary(1))), math.log2(w))
#    t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
#                convertToBinary(1))), math.log2(w))
#    a = binadd(lRotate(binxor(a, t), u), s[2 * i])
#    c = binadd(lRotate(binxor(c, u), t), s[2 * i + 1])
#    a = b
#    b = c
#    c = d
#    d = a
# a = binadd(a, s[t - 2])
# c = binadd(c, s[t - 1])
###########################################################################


encryptedChain = [a, b, c, d]

# print("encrypted")
# print(encryptedChain)

# create a new image
# im = Image.new(mode="RGB", size=(4, 4))
# im = Image.new(mode="RGB", size=(3, 3))

# rebuild(encryptedChain, im)
print("starting rebuild")
rebuild(encryptedChain, image)

image.save("encryptedImage.png")
