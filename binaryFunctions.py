#functions
def convertToBinary(x):
    rturn = ""
    adding = 0
    while (x > 0):
        adding = x % 2
        rturn = str(adding) + rturn
        x = x // 2
    rturn = str(rturn)
    if len(rturn) > 8:
        print("number to large(greater than 8 bits)")
    while len(rturn) < 8:
        rturn = "0"+rturn
    return rturn
def convertToInt(x):
    #turns binary to int
    x
def lRotate(x):
    #rotatates left
    x
def rRotate(x):
    #rotates right
    x
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