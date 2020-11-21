import libcst
code = """
from Crypto.Util.number import *
from secret import flag
from gmpy2 import gcd,invert

L = lambda x,n: (x-1) // n
mask = 0x1000000000000000000000000000000000000000001000000000000000000000000000000000000000001000000000000000000000000000000000000000001000000000000000000000000000000000000000001000000000000000000000000000000000000000001


def genkey(q_len):
    while True:
        q = getStrongPrime(q_len)
        x = getRandomNBitInteger(21 * 8)
        p = (0b11 << (q_len - 2)) + (mask * x << 32) + getRandomNBitInteger(32) | 1
        if isPrime(p) and gcd(p*q, (p-1)*(q-1)) == 1:
            n = p * q
            break
    
    lam = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
    while True:
        g = getRandomRange(1,n**2)
        t = L(pow(g,lam,n**2),n)
        if gcd(t, n) == 1:
            mi = invert(t,n)
            break
    return n, g


def encrypt(em, en, eg):
    while True:
        r = getRandomRange(1,en)
        if gcd(r, en) == 1:
            break
    return pow(eg,em,en**2) * pow(r,en,en**2) % en ** 2

        
n,g = genkey(1024)
m = bytes_to_long(flag)
c = encrypt(m,n,g)

with open('./output','w') as f:
    f.write(str(n))
    f.write(str(c))
    f.write(str(g))
"""

with open('./code','w') as f:
    f.write(str(libcst.parse_module(code)))