# default values
K = 1
m = 128


def encrypt(plain_text, key=K):
    return process(e, plain_text, key)


def decrypt(cipher_text, key=K):
    return process(d, cipher_text, key)


def process(fnc, text, key):
    ordinals = [ord(x) for x in text]
    result = [fnc(x, key) for x in ordinals]
    return "".join(chr(x) for x in result)


def e(ordinal, key):
    return (ordinal + key) % m


def d(cipher, key):
    return (cipher - key) % m
