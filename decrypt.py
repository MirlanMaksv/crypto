#! /usr/bin/python3

import sys
import ceasar, affine
from word_loader import words_dict as words


def found_words(text):
    total = 0
    for word in text.split(" "):
        if words.get(word):
            total += 1
    return total


def ceasar_attack(cipher):
    print("------ Using Ceasar Cipher ------")
    for key in range(1, 15):
        text = ceasar.decrypt(cipher, key)
        total = found_words(text)
        if total > 0:
            print(f"Found '{text}'")

    print("------" * 6)
    return False

def affine_attack(cipher):
    print("------ Using Affine Cipher ------")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cipher = sys.argv[1]

        found = ceasar_attack(cipher)
        if not found:      
            found = affine_attack(cipher)
        if not found:
            pass