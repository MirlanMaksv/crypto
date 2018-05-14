from sympy.crypto.crypto import encipher_vigenere, decipher_vigenere
from smp.symbols import symbols


def encrypt(msg, key):
    return encipher_vigenere(msg, key, symbols=symbols)


def decrypt(cipher, key):
    return decipher_vigenere(cipher, key, symbols=symbols)
