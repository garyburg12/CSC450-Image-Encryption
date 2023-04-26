#functions
def convertToBinary(x):
    rturn = []
    adding = 0
    while (x > 0):
        adding = x % 2
        rturn=[adding] + rturn
        x = x // 2
    while len(rturn) < 8:
        rturn = [0]+rturn
    return rturn
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
        print (z)
        print (total)
        if x[i] == 1:
           total+=z
        z=z*2
    return total
    
    
def lRotate(x):
    x=x[1:]+[x[0]]
    return x
def rRotate(x):
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
def binmult(x):
    #convert bin to int 
    x