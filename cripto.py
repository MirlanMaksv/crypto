#! /usr/bin/python3

import sys


if len(sys.argv) > 2:
    cipherName = sys.argv[1].lower()
    message = sys.argv[2]
    print("Encrypting '{0}' using '{1} Cipher'".format(message, cipherName.capitalize()))
    cryptoMethod = __import__(cipherName)
    
    encryptedText = cryptoMethod.encrypt(message)      
    print("Encrypted text --", encryptedText)

    decryptedText = cryptoMethod.decrypt(encryptedText)
    print("Decrypted text --", decryptedText)

else:
    print('''Provide cipher method and message
    Usage: cripto [cipher method to apply] [text]
    Cipher methods: ceasar, affine''')
