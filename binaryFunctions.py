#functions
def convertToBinary(x):
    binlist = []
    adding = 0
    while (x > 0):
        adding = x % 2
        binlist=[adding] + binlist
        x = x // 2
    while len(binlist) < 8:
        binlist = [0]+binlist
    return binlist
def convertToInt(x):
    y=0
    for i in x:
        if i != 1:
            y+=1
        else:
            break
    z=1
    total=0
    for i in range(len(x) - 1, y - 1, -1):
        if x[i] == 1:
           total+=z
        z=z*2
    return total
    
    
def lRotate(x, y):
    for i in range (0, y):
        x=x[1:]+[x[0]]
    return x
def rRotate(x, y):
    for i in range (0, y):
        x=[x[-1]]+x[0:-1]
    return x
def binxor(x):
    #XOR function
    x
def binadd(x):
    #binary addition
    x
def binsub(x):
    #binary subtraction
    x
def binmult(x, y):
    x = convertToInt(x)
    y = convertToInt(y)
    rvalue = x * y
    rvalue = convertToBinary(rvalue)
    return rvalue