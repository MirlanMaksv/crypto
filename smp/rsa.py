from sympy.crypto.crypto import encipher_rsa, decipher_rsa, rsa_private_key, rsa_public_key
from smp.symbols import symbols


def encrypt(msg, pqe=(10007, 103, 211)):
    ne = rsa_public_key(*pqe)
    nlength = len(str(ne[0]))
    m = ""
    # if len(msg) < nlength:
    #     msg = msg.ljust(nlength, "x")
    # elif len(msg) % nlength != 0:
    #     msg = msg[:-nlength] + msg[-(len(msg) % nlength):].ljust(nlength, "x")
    for x in msg:
        m += str(symbols.index(x)).zfill(2)

    if len(m) < nlength:
        m = m.ljust(nlength, "0")
    elif len(m) % nlength != 0:
        m = m[:-nlength] + m[-(len(m) % nlength):].ljust(nlength, "0")

    M = split_by_step(m, nlength - 1)
    cipher = ""
    for i in M:
        enciphered = encipher_rsa(i, ne)
        cipher += str(enciphered).zfill(nlength)
    return cipher


def decrypt(cipher, pqe=(10007, 103, 211)):
    nd = rsa_private_key(*pqe)
    nlength = len(str(nd[0]))
    cipher = split_by_step(cipher, nlength)
    m = ""
    for c in cipher:
        m += str(decipher_rsa(c, nd)).zfill(nlength - 1)
    msg = ""
    print(split_by_step(m, 2))
    for ordinal in split_by_step(m, 2):
        msg += symbols[int(ordinal)]
    return msg


def split_by_step(string, step):
    step = step if step < len(string) else len(string)
    return [int(string[i:i + step]) for i in range(0, len(string), step)]


print(decrypt(encrypt("themagice")))
