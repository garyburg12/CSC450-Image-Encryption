import math
from binaryFunctions import *
# key length
b = 8

# secret key
k = [1, 5, 2, 8, 3, 4, 4, 2]

# convert ints to binary

for i in range(0, b):
    k[i] = convertToBinary(k[i])

# print(k)
print(convertToBinary(0))
