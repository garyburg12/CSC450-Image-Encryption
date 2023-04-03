import math
import numpy as np
import array as arr

# size of word block 16, 32, or 64
w = 16

# number of rounds
r = 5

# key length
b = 16

# secret key not sure how this works
k = []

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


def RightRotate(A, K):
    old = A
    new = [0]*len(A)
    for i in range(K):
        new[0] = old[-1]
        new[1:] = old[:-1]
        old = new.copy()
    return new


def LeftRotate(l, n):
    return l[-n % len(l):] + l[:-n % len(l)]


# Key expansion

# convert secret key from bytes to words
l = []

u = w/8

# length of new array l
c = b/u

i = b - 1
while i >= 0:
    l[i/u] = (l[i/u] << < 8) + k[i]


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
