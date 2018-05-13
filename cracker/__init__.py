from sympy.crypto.crypto import decipher_shift, decipher_affine, decipher_vigenere
from sympy.ntheory.primetest import isprime
from itertools import permutations as generatepermutations
from smp.symbols import symbols
from words_loader import words_dict as words
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

    n = len(symbols)
    for a in relprimes(n):
        for b in range(n):
            decrypt(decipher_affine, (a, b), cipher)

    print("-"*len(name), end="\n\n")


def vigenere(cipher, **kwargs):
    name = intro.format("Vigenere")
    print(name)

    # max key length is 4
    for i in range(1, 4):
        permutations = list(generatepermutations(symbols, i))
        for p in permutations:
            decrypt(decipher_vigenere, p, cipher)

    print("-"*len(name), end="\n\n")


def hill(cipher, **kwargs):
    name = intro.format("Hill's")
    print(name)

    # TODO: Invertible matrix generator is needed

    print("-"*len(name), end="\n\n")
