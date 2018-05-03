from sympy.crypto.crypto import encipher_shift, decipher_shift
from sympy.crypto.crypto import encipher_affine, decipher_affine
from sympy.crypto.crypto import encipher_vigenere, decipher_vigenere
from sympy.crypto.crypto import encipher_hill, decipher_hill
from sympy.crypto.crypto import encipher_rsa, decipher_rsa, rsa_private_key, rsa_public_key
from smp.symbols import symbols


def caesar(msg, key, **kwargs):
    et = encipher_shift(msg, key, symbols=symbols)
    dt = decipher_shift(et, key, symbols=symbols)
    return et, dt


def affine(msg, key, **kwargs):
    et = encipher_affine(msg, key, symbols=symbols)
    dt = decipher_affine(et, key, symbols=symbols)
    return et, dt


def vigenere(msg, key, **kwargs):
    et = encipher_vigenere(msg, key, symbols=symbols)
    dt = decipher_vigenere(et, key, symbols=symbols)
    return et, dt


def autoclave(msg, key, **kwargs):
    key = key + msg[:len(msg) - len(key)]
    return vigenere(msg, key, **kwargs)


def hill(msg, key, **kwargs):
    et = encipher_hill(msg, key, symbols=symbols, pad="0")
    dt = decipher_hill(et, key, symbols=symbols)
    return et, dt


def rsa(msg, pqe, **kwargs):
    nd = rsa_private_key(*pqe)
    ne = rsa_public_key(*pqe)
    nlength = len(str(ne[0]))
    m = []
    for x in msg:
        ordinal = ord(x)
        m.append(ordinal)

    cipher = []
    for i in m:
        enciphered = encipher_rsa(i, ne)
        cipher.append(enciphered)

    m = []
    for c in cipher:
        m.append(decipher_rsa(c, nd))

    dt = "".join([chr(x) for x in m])
    return cipher, dt


def split_by_step(s, n):
    return [int(s[i:i+n]) for i in range(0, len(s), n)]
