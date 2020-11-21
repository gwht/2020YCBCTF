from Crypto.Util.number import getPrime,bytes_to_long,getRandomNBitInteger
from secret import flag
from gmpy2 import gcd


def gmc(a, p):
    if pow(a, (p-1)//2, p) == 1:
        return 1
    else:
        return -1


def gen_key():
    [gp,gq] = [getPrime(512) for i in range(2)]
    gN = gp * gq
    return gN, gq, gp


def gen_x(gq,gp):
    while True:
        x = getRandomNBitInteger(512)
        if gmc(x,gp) ^ gmc(x,gq) == -2:
            return x


def gen_y(gN):
    gy_list = []
    while len(gy_list) != F_LEN:
        ty = getRandomNBitInteger(768)
        if gcd(ty,gN) == 1:
            gy_list.append(ty)
    return gy_list


if __name__ == '__main__':

    flag = bin(bytes_to_long(flag))[2:]
    F_LEN = len(flag)
    N, q, p = gen_key()
    x = gen_x(q, p)
    y_list = gen_y(N)
    ciphertext = []

    for i in range(F_LEN):
        tc = pow(y_list[i],2) * pow(x,int(flag[i])) % N
        ciphertext.append(tc)

    with open('./output.txt','w') as f:
        f.write(str(N) + '\n')
        for i in range(F_LEN):
            f.write(str(ciphertext[i]) + '\n')

