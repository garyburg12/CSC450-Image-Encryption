# from PIL import Image
from PIL import *
from binaryFunctions import *
from keyExpansion import *
from imageConversion import *
# Import an image from directory:
# image = Image.open("checker.png")
image = Image.open("msu50.png")

print("starting block chain")
blockchain = blockChain(image, 0)

# print("block chain")
# print(blockchain)

a = blockchain[0] 
b = blockchain[1]
c = blockchain[2]
d = blockchain[3]
log2size=2
while pow(2, log2size) < len(a):
    log2size+=1
    print(log2size)
log2size=pow(2, log2size)
print(log2size)
log2size=log2size-len(a)
print(log2size)
a=a+a[:log2size]
b=b+b[:log2size]
c=c+c[:log2size]
d=d+d[:log2size]
log2size=len(a)
print(len(a))
print(len(b))
print(len(c))
print(len(d))
# start encryption
print("starting encryption")
b = binadd(b, s[0])
d = binadd(d, s[1])
i = 1
for i in range(1, r + 1):
    # t = (B x (2 * B + 1)) <<< log(w)
    print("round " + str(i))
    #t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
    #            convertToBinary(1))), int(math.log2(log2size)))
    # t = lRotate(multmod2(b, binadd(binmult(convertToBinary(2), b),
    #            convertToBinary(1))), int(math.log2(w)))

    plat = binmult(convertToBinary(2), b)
    #print(len(plat))
    cork = binadd(plat, convertToBinary(1))
    #print(len(cork))
    spook = multmod2(b, cork)
    #print(spook)
    banana = log2size
    print(math.log2(banana))
    t = lRotate(spook, banana)

    # u = (D X (2 * D + 1)) <<< log(w)
    u = lRotate(multmod2(d, binadd(binmult(convertToBinary(2), d),
                convertToBinary(1))), int(math.log2(log2size)))  # was int(math.log2(w)
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
    
    #a, b, c, d = b, c, d, a
    temp = a
    a = b
    b = c
    c = d
    d = temp
    print(a)
    print(b)
    print(c)
    print(d)
    #print(t)
a = binadd(a, s[m - 2])
c = binadd(c, s[m - 1])

encryptedChain = [a, b, c, d]
print(encryptedChain)
print("encrypted")
# print(encryptedChain)
distance = len(a) + len(b) + len(c) + len(d)
distance = distance / 24
width, height = image.size
while distance > width * height:
    height += 1
while width * height > distance:
    d.append(0)
    distance +=1
print("starting rebuild")
#image = rebuild(encryptedChain, image)
image = rebuild(encryptedChain, width, height)
print(blockChain(image, 1))
image.save("encryptedImage.png")
