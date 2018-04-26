from sympy.crypto.crypto import decipher_shift
from smp.symbols import symbols
from words_loader import words_dict as words

intro = "---------- | {} crypto system | ----------"


def crack(**kwargs):
    caesar(kwargs)


def caesar(cipher):
    name = intro.format("Caesar")
    print(name)
        
    print("-"*len(name), end="\n\n")


def affine(cipher):
    name = intro.format("Affine")
    print(name)

    print("-"*len(name), end="\n\n")


def vigenere(cipher):
    name = intro.format("Vigenere")
    print(name)

    print("-"*len(name), end="\n\n")


def hill(cipher):
    name = intro.format("Hill's")
    print(name)

    print("-"*len(name), end="\n\n")
