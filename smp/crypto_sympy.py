from sympy.crypto.crypto import encipher_shift, decipher_shift
from sympy.crypto.crypto import encipher_affine, decipher_affine
from sympy.crypto.crypto import encipher_vigenere, decipher_vigenere
from sympy.crypto.crypto import encipher_hill, decipher_hill
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


def hill(msg, key, **kwargs):
    et = encipher_hill(msg, key, symbols=symbols, pad="0")
    dt = decipher_hill(et, key, symbols=symbols)
    return et, dt
