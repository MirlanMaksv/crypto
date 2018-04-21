from sympy.crypto.crypto import encipher_shift, decipher_shift
from sympy.crypto.crypto import encipher_affine, decipher_affine
from sympy.crypto.crypto import encipher_vigenere, decipher_vigenere
from symbols import symbols

def caesar(msg="", key=0, **kwargs):
    et = encipher_shift(msg, key, symbols=symbols)
    dt = decipher_shift(et, key, symbols=symbols)
    return et, dt


def affine(msg="", ab=(), **kwargs):
    et = encipher_affine(msg, ab, symbols=symbols)
    dt = decipher_affine(et, ab, symbols=symbols)
    return et, dt
