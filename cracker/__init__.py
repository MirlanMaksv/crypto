from sympy.crypto.crypto import decipher_shift
from smp.symbols import symbols
from words_loader import words_dict as words

intro = "---------- | {} crypto system | ----------"


def crack(**kwargs):
    caesar(**kwargs)
    affine(**kwargs)
    vigenere(**kwargs)
    hill(**kwargs)

def caesar(cipher, **kwargs):
    name = intro.format("Caesar")
    print(name)
    n = len(symbols)
    for i in range(n):
        decrypted = decipher_shift(cipher, i, symbols=symbols)
        if words.get(decrypted):
            print("Found", decrypted)

    print("-"*len(name), end="\n\n")


def affine(cipher, **kwargs):
    name = intro.format("Affine")
    print(name)

    print("-"*len(name), end="\n\n")


def vigenere(cipher, **kwargs):
    name = intro.format("Vigenere")
    print(name)

    print("-"*len(name), end="\n\n")


def hill(cipher, **kwargs):
    name = intro.format("Hill's")
    print(name)

    print("-"*len(name), end="\n\n")
