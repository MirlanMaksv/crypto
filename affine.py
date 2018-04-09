# default values
A, B = 343, 8
m = pow(2, 31)


def encrypt(plain_text, a=A, b=B):
    return process(e, plain_text, a, b)


def decrypt(cipher_text, a=A, b=B):
    a_inverse = find_inverse(a)
    return process(d, cipher_text, a_inverse, b)


def process(fnc, text, a, b):
    ordinals = [ord(char) for char in text]
    result = [fnc(e, a, b) for e in ordinals]
    return "".join([chr(x) for x in result])


def e(p, a, b):
    return (a * p + b) % m


def d(c, a_inverse, b):
    return (a_inverse * (c - b)) % m


def find_inverse(a):
    x = 1
    while x % a != 0:
        x += m
    return x // a
