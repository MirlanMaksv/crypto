from smp import vigenere


def encrypt(msg, key):
    key = key + msg[:len(msg) - len(key)]
    return vigenere.encrypt(msg, key)


def decrypt(cipher, key):
    return vigenere.decrypt(cipher, key)
