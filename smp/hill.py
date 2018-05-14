from sympy.crypto.crypto import encipher_hill, decipher_hill
from smp.symbols import symbols


def encrypt(msg, key):
    return encipher_hill(msg, key, symbols=symbols)


def decrypt(cipher, key):
    return decipher_hill(cipher, key, symbols=symbols)
