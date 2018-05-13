from smp.symbols import symbols


def encrypt(pk, n):
    length = len(pk)
    binary = bin(n)[2:].zfill(length)
    s = 0
    for i in range(length):
        s += pk[i] * int(binary[i])
    return s


def merkle_hellman(msg, S, a, mod, **kwargs):
    # encrypting
    x0 = find_x0(a, mod)
    pk = public_key(S, a, mod)
    M = [ord(char) for char in msg]
    cipher = [encrypt(pk, m) for m in M]

    # decrypting
    C = [c * x0 % mod for c in cipher]
    binaries = []
    for c in C:
        res = knapsack(S, c)
        if res == -1:
            raise Exception("Knapsack problem can't be solved for {} and {}".format(S, c))
        binaries.append(res)

    text = "".join([chr(int(b, 2)) for b in binaries])
    return cipher, text


def public_key(S, a, mod):
    return [s * a % mod for s in S]


def find_x0(a, mod):
    x = 1
    while x % a != 0:
        x += mod
    return x // a


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
