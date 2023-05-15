from PIL import Image
from binaryFunctions import *
from keyExpansion import *
from imageConversion import *
# Import an image from directory:
image = Image.open("encryptedImage.png")

print("starting block chain")
blockchain = blockChain(image)

a = blockchain[0]
b = blockchain[1]
c = blockchain[2]
d = blockchain[3]

# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))


# start decryption
print("starting decryption")
c = binsub(c, s[m - 1])
a = binsub(a, s[m - 2])
i = r
for i in range(r, 0, -1):

    a, b, c, d = d, a, b, c

    # u = (D X (2 * D + 1)) <<< log(w)
    u = lRotate(multmod2(d, binadd(binmult(convertToBinary(2), d),
                convertToBinary(1))), int(math.log2(w)))  # adding 1

    # t = (B x (2 * B + 1)) <<< log(w)
    t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
                convertToBinary(1))), int(math.log2(w)))  # adding 1

    # C = ((C - S[2 * i + 1]) >>> t) ^ u
    c = binxor(rRotate(binsub(c, s[(2 * i) + 1]), convertToInt(t)), u)

    # A = ((A - S[2 * i]) >>> u) ^ t
    a = binxor(rRotate(binsub(a, s[2 * i]), convertToInt(u)), t)

    # while len(a) < 60000:
    #    a.append(0)
    # while len(b) < 60000:
    #    b.append(0)
    # while len(c) < 60000:
    #    c.append(0)
    # while len(d) < 60000:
    #    d.append(0)

    print(t)

d = binsub(d, s[1])
b = binsub(b, s[0])

# d.append(0)
# d.append(0)

decryptedChain = [a, b, c, d]

# create a new image
# im = Image.new(mode="RGB", size=(50, 50))
im = Image.new(mode="RGB", size=(100, 100))

# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))

print("starting rebuild")
rebuild(decryptedChain, im)

im.save("decryptedImage.png")
