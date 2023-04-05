import math
import numpy as np
import array as arr

# variables
# w = word size
# r = rounds (changes size t of key table)
# b = length of secret key
# k[] = secret key array converted to binary of size b
# p = magical constant
# q = magical constatnt


# size of word block 16, 32, or 64
w = 16

# number of rounds
r = 5

# key length
b = 16

# secret key not sure how this works
k = ["b", "l", "o", "c", "k"]


# Eulers number
e = math.e

# Golden ratio
g = (1 + math.sqrt(5))/2

# return closest odd integer


def Odd(x):
    return np.ceil(x)


# magical constant p
p = Odd((e - 2) * 2**w)

# magical constant q
q = Odd((g - 1) * 2**w)

# cylic roations

# In-place rotates s towards left by d


def leftrotate(s, d):
    tmp = s[d:] + s[0: d]
    return tmp

# In-place rotates s
# towards right by d


def rightrotate(s, d):

    return leftrotate(s, len(s) - d)


# Key expansion

# convert secret key from bytes to words

u = w/8

# length of new array l
c = b/u

# initialize l with 0
l = [0] * c

i = b - 1
while i >= 0:
    l[i/u] = leftrotate(l, 8) + k[i]
    i = i - 1


# size of s-table array
t = 2(r + 2)

# initialize array
s = []
s[0] = p

i = 1
for i in t - 1:
    s[i] = s[i-1] + q


# key mixing

a, b, i, j = 0


for k in (3 * (2 * r + 4)):  # or max(t, c)
    s[i] = (s[i] + a + b) << < 3
    a = s[i]
    l[j] = (l[j] + a + b) << < (a + b)
    i = (i + 1) % t
    j = (j + 1) % c
