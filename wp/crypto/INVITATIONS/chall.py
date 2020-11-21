from Crypto.Util.number import getPrime, bytes_to_long
from secret import flag
import gmpy2
import random



def pad(s,i):
    return i * pow(3,s.bit_length()) + s**2

def gen_N():
    return getPrime(512) * getPrime(512)


assert len(flag) == 54
invite = bytes_to_long(flag)

e_list = [random.choice([3,5,7]) for i in range(14)]
N_list = [gen_N() for i in range(14)]

with open('./invitations','w') as f:
    for i in range(14):
        invis = pow(pad(invite,i+1),e_list[i],N_list[i])
        f.write('Invitation%d: %d \n'%(i+1,invis))

    f.write('Wait a minute! \n')

    for i in range(14):
        f.write('[e%d,N%d]: [%d,%d]\n'%(i+1,i+1,e_list[i],N_list[i]))
