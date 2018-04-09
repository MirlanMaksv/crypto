#! /usr/bin/python3

import sys


def parseArg(arg):
    sublist = arg.split("=")
    sublist[1] = int(sublist[1])
    return sublist
    

if __name__ == "__main__":
    if len(sys.argv) > 2:
        cryptoMethodName = sys.argv[1].lower()
        message = sys.argv[2]
        kwargs = dict(parseArg(arg) for arg in sys.argv[3:])

        print(f"Encrypting '{message}' using '{cryptoMethodName.capitalize()} Cipher'")
        cryptoMethod = __import__(path + cryptoMethodName)
        
        encryptedText = cryptoMethod.encrypt(message, **kwargs)
        print("Encrypted text --", encryptedText)

        decryptedText = cryptoMethod.decrypt(encryptedText, **kwargs)
        print("Decrypted text --", decryptedText)

    else:
        print('''Provide cipher method and message
        Usage: cripto [cipher method to apply] [text]
        Cipher methods: ceasar, affine''')
