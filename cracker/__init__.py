from sympy.crypto.crypto import decipher_shift, decipher_affine
from smp.symbols import symbols
from words_loader import words_dict as words
from sympy.ntheory.primetest import isprime
from common import relprimes

intro = "---------- | {} crypto system | ----------"


def decrypt(fnc, key, cipher):
    decryptedText = fnc(cipher, key, symbols=symbols)
    foundWords = [word for word in decryptedText.split() if words.get(word)]
    if len(foundWords) > 0:
        print("FOUND", foundWords)


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
        decrypt(decipher_shift, i, cipher)

    print("-"*len(name), end="\n\n")


def affine(cipher, **kwargs):
    name = intro.format("Affine")
    print(name)

    length = len(symbols)
    for a in relprimes(length):
        for b in range(length):
            decrypt(decipher_affine, (a, b), cipher)

    print("-"*len(name), end="\n\n")


def vigenere(cipher, **kwargs):
    name = intro.format("Vigenere")
    print(name)

    

    print("-"*len(name), end="\n\n")


def hill(cipher, **kwargs):
    name = intro.format("Hill's")
    print(name)

    print("-"*len(name), end="\n\n")
