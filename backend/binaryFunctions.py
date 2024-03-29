import math
# functions


def convertToBinary(x):
    binlist = []
    if (x == 0):
        return [0, 0, 0, 0, 0, 0, 0, 0]
    logofx = int(math.log2(x))
    buffer0s = 7-logofx
    while len(binlist) < buffer0s:
        binlist.append(0)
    twotoi = pow(2, logofx)
    for i in range(logofx, -1, -1):
        if x >= twotoi:
            binlist.append(1)
            x = x-twotoi
        else:
            binlist.append(0)
        twotoi = twotoi//2
    return binlist


def convertToInt(x):
    z = 1
    total = 0
    for i in range(len(x)-1, -1, -1):
        if x[i] == 1:
            total += z
        z = z*2
    return total


def lRotate(x, y):
    y = y % len(x)
    for i in range(0, y):
        x = x[1:]+[x[0]]
    return x


def rRotate(x, y):
    y = y % len(x)
    for i in range(0, y):
        x = [x[-1]]+x[0:-1]
    return x


def binxor(x, y):
    while len(y) < len(x):
        y = [0]+y
        # y = y+[0] ask about this
    while len(y) > len(x):
        x = [0]+x
        # y = y+[0] ask about this

    for i in range(0, len(x)):
        if x[i] == y[i]:
            x[i] = 0
        else:
            x[i] = 1
    return x


# def binadd(x, y):
#    if len(x) < len(y):
#        while len(x) < len(y):
#            x = [0]+x
#    if len(x) > len(y):
#        while len(x) > len(y):
#            y = [0]+y
#
#    rvalue = []
#    for i in range(0, len(x)):
#        rvalue[i] = x


#    return y

def binadd(x, y):
    x = convertToInt(x)
    y = convertToInt(y)
    rvalue = x + y
    # added this for mod 2^w
    # rvalue = (x + y) % (2 ^ 32)
    rvalue = convertToBinary(rvalue)
    return rvalue


def binsub(x, y):
    x = convertToInt(x)
    y = convertToInt(y)
    rvalue = x - y
    # added this for mod 2^w
    # rvalue = (x - y) % (2 ^ 32)
    rvalue = convertToBinary(rvalue)
    return rvalue


def binmult(x, y):
    x = convertToInt(x)
    y = convertToInt(y)
    rvalue = x * y
    rvalue = convertToBinary(rvalue)
    return rvalue


def multmod2(x, y):
    x = convertToInt(x)
    y = convertToInt(y)
    # rvalue = (x * y) % (2 ^ 16) CHANGIN THIS LINE FOR NOW
    # rvalue = (x * y)
    rvalue = (x * y) % (2 ^ 32)
    rvalue = convertToBinary(rvalue)
    return rvalue
