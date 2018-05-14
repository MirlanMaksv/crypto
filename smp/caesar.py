from sympy.crypto.crypto import encipher_shift, decipher_shift
from smp.symbols import symbols


def encrypt(msg, key):
    return encipher_shift(msg, key, symbols=symbols)


def decrypt(cipher, key):
    return decipher_shift(cipher, key, symbols=symbols)
