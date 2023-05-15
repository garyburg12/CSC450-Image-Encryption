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
log2size=2

a = blockchain[0] 
b = blockchain[1]
c = blockchain[2]
d = blockchain[3]

while pow(2, log2size) < len(a):
    log2size+=1
log2size=pow(2, log2size)
log2size=len(a)-i
a=a+a[:i]
b=b+b[:i]
c=c+c[:i]
d=d+d[:i]

# start encryption
print("starting encryption")
b = binadd(b, s[0])
d = binadd(d, s[1])
i = 1
for i in range(1, r + 1):
    # t = (B x (2 * B + 1)) <<< log(w)
    print("round finished")
    t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
                convertToBinary(1))), int(math.log2(w) - 1))
    # t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
    #            convertToBinary(1))), int(math.log2(w)))

    plat = binmult(convertToBinary(3), b)
    print(len(plat))
    cork = binadd(plat, convertToBinary(1))
    print(len(cork))
    spook = multmod2(b, cork)
    print(spook)
    banana = int(math.log2(w))
    print(banana)
    t = lRotate(spook, banana)

    # u = (D X (2 * D + 1)) <<< log(w)
    u = lRotate(multmod2(d, binadd(binmult(convertToBinary(2), d),
                convertToBinary(1))), int(math.log2(w) - 1))  # was int(math.log2(w)
    # A = ((A ^ t) <<< u) + S[2 * i]
    a = binadd(lRotate(binxor(a, t), convertToInt(u)), s[2 * i])

    # C = ((C ^ u) <<< t) + S[2 * i + 1]
    c = binadd(lRotate(binxor(c, u), convertToInt(t)), s[(2 * i) + 1])

    # while len(a) < 60000:
    #   a.append(0)
    # while len(b) < 60000:
    #    b.append(0)
    # while len(c) < 60000:
    #   c.append(0)
    # while len(d) < 60000:
    #    d.append(0)
    # print(len(a))
    # print(len(b))
    # print(len(c))
    # print(len(d))

    a, b, c, d = b, c, d, a

    print(t)
a = binadd(a, s[m - 2])
c = binadd(c, s[m - 1])

encryptedChain = [a, b, c, d]

print("encrypted")
# print(encryptedChain)

print("starting rebuild")
rebuild(encryptedChain, image)

image.save("encryptedImage.png")
