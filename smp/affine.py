from sympy.crypto.crypto import encipher_affine, decipher_affine
from smp.symbols import symbols


def encrypt(msg, key):
    return encipher_affine(msg, key, symbols=symbols)


def decrypt(cipher, key):
    return decipher_affine(cipher, key, symbols=symbols)
