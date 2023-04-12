import math

# variables
# w = word size
# r = rounds (changes size t of key table)
# b = length of secret key
# k[] = secret key array converted to binary of size b
# s[] = expanded key table
# t = size of s[]   2(r + 2)
# l[] = array k[] but in size words instead of bytes
# u = bytes per word

# 1 byte = 8 bits
# 1 word = 16/32/64 bits

# r, g, b are each 8 bits = 24 bits total
# A, B, C, D = 6 bits each


# size of word block 16, 32, or 64
w = 16

# number of rounds
r = 5

# key length
b = 8

# secret key
k = [1, 5, 2, 8, 3, 4, 4, 2]


# Eulers number
e = math.e

# Golden ratio
g = (1 + math.sqrt(5))/2

# return closest odd integer


def Odd(x):
    x = math.floor(x)
    if (x % 2 == 0):
        x = x + 1
    return x


# magical constant p
# p = Odd((e - 2) * 2**w)
p = Odd((e - 2) * pow(2, w))
print("p")
print(p)

# magical constant q
# q = Odd((g - 1) * 2**w)
q = Odd((g - 1) * pow(2, w))
print("q")
print(q)

# modified integer to binary converter


def binary(x):
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

# cylic roation is bit rotation, 16 << 2 = 64

# Key expansion

# convert secret key from bytes to words


# number of bytes per word
u = w//8

# length of new array l
c = b//u

# initialize l with 0, l contains words
l = ["x"] * c

i = b - 1

for i in range(i, -1, -1):
    # this needs to append the binary of k[i] to l[i//u] but right now its just adding it
    if l[i//u] == "x":
        l[i//u] = binary(k[i])
    else:
        l[i//u] = l[i//u] + binary(k[i])
    # l[i//u] = (l[i//u]) + k[i]
    # l[i//u] = (bin(l[i//u] << 8)) + bin(k[i])
    # print(l[i//u])
print(l[3])
print(l[2])
print(l[1])
print(l[0])
# instead of doing left bit rotation
# convert each number in k to binary, store as a list of lists
# first iteration, put list k[i] into l[i//u]
# next iteration

# for example, b = 8, w = 16, u = 2, k = [1, 5, 2, 8, 3, 4, 4, 2]
# k = [00000001, 00000101, 00000010, 00001000, 00000011, 00000100, 00000100, 00000010]
#
# first iteration
# l[7//2] ---> l[3] = 0 + k[7]        ---> l[3] = 00000010
# l[6//2] ---> l[3] = 00000010 + k[6] ---> l[3] = 0000001000000100
# l[5//2] ---> l[2] = 0 + k[5]        ---> l[2] = 00000100
# l[4//2] ---> l[2] = 00000100 + k[4] ---> l[2] = 0000010000000011


# size of s-table array
t = 2 * (r + 2)

# initialize s[] key table
s = [p]
# make s[0] == p
# s[] = p

i = 1
for i in range(i, t - 1):
    s.append(s[i-1] + q)
    # s[i] = s[(i-1)] + q
print(s[0])
print(s[1])
print(s[2])
print(s[3])

# key mixing

i = 0
j = 0
a = 0
b = 0

# x is dummy variable just run through 3 * max(t, c) times
for x in range((3 * max(t, c))):
    s[i] = (s[i] + a + b) << 3
    a = s[i]
    # currently have overflow error here
    l[j] = (l[j] + a + b) << (a + b)
    b = l[j]
    i = (i + 1) % t
    j = (j + 1) % c

print(*s)
