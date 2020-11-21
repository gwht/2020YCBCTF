from Crypto.Util.number import long_to_bytes
import gmpy2
plaintext = ''
with open('output.txt') as f:
    n = int(f.readline())
    for line in f:
        cipher = int(line)
        if gmpy2.jacobi(cipher,n) == -1:
            plaintext += '1'
        else:
            plaintext += '0'
print(long_to_bytes(int(plaintext,2)))


