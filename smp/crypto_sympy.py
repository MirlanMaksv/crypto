#! /usr/bin/python3
from sympy.crypto.crypto import encipher_shift, decipher_shift
from sympy.crypto.crypto import encipher_affine, decipher_affine
from parser import args
from symbols import symbols

print(args)

if __name__ == "__main__":
    cryptoMethod = args.crypto.lower()
    if cryptoMethod == 'caesar':
        et = encipher_shift(args.msg, args.key, symbols=symbols)
        dt = decipher_shift(et, args.key, symbols=symbols)
    elif cryptoMethod == "affine":
        pass
    
    print("encrypted text -->", et)
    print("decrypted text -->", dt)
