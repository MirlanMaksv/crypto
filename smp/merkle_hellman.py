from smp.symbols import symbols
from common import arelprimes


def encrypt(msg, S, a, mod):
    if not arelprimes(a, mod):
        raise Exception("{} and {} must be relatively prime numbers".format(a, mod))
    # encrypting
    pk = public_key(S, a, mod)
    M = [ord(char) for char in msg]
    cipher = [compute(pk, m) for m in M]
    return cipher


def decrypt(cipher, S, a, mod):
    if not arelprimes(a, mod):
        raise Exception("{} and {} must be relatively prime numbers".format(a, mod))
    # decrypting
    x0 = find_x0(a, mod)
    binaries = []
    for c in cipher:
        c = c * x0 % mod
        res = knapsack(S, c)
        if res == -1:
            raise Exception("Knapsack problem can't be solved for {} and {}".format(S, c))
        binaries.append(res)

    msg = "".join([chr(int(b, 2)) for b in binaries])
    return msg


def compute(pk, n):
    length = len(pk)
    binary = bin(n)[2:].zfill(length)
    s = 0
    for i in range(length):
        s += pk[i] * int(binary[i])
    return s


def public_key(S, a, mod):
    return [s * a % mod for s in S]


def find_x0(a, mod):
    x = 1
    while x % a != 0:
        x += mod
    return x // a


# super increasing sequence knapsack problem solver
def knapsack(S, n):
    binary = ""
    for i in range(len(S)):
        if n >= S[-i - 1]:
            binary += "1"
            n -= S[-i - 1]
            if n == 0:
                break
        else:
            binary += "0"

    return -1 if n != 0 else binary[::-1].zfill(len(S))
