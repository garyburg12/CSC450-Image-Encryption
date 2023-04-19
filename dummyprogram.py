import math
def binary(x):
    rturn = ""
    adding = 0
    while (x > 0):
        adding = x % 2
        rturn = str(adding) + rturn
        x = x // 2
    rturn=str(rturn)
    if len(rturn) > 8:
        print("number to large(greater than 8 bits)")
    while len(rturn) < 8:
        rturn="0"+rturn
    return rturn

print((math.e-2) * (2**16))