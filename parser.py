from smp.crypto_sympy import caesar, affine, vigenere, hill
from cracker import crack
from sympy import Matrix
import argparse

descr = "Encryption and decryption using sympy package"
parent = argparse.ArgumentParser(add_help=False)
parent.add_argument("-m", "--msg", type=str, required=True, help="Message to be encrypted then decrypted")

parser = argparse.ArgumentParser(description=descr)
subparsers = parser.add_subparsers(dest="crypto")

caesarparser = subparsers.add_parser("caesar", help="Caesar crypto system", parents=[parent])
caesarparser.add_argument("-k", "--key", type=int, required=True, help="Key to be used in encryption")
caesarparser.set_defaults(func=caesar)

affineparser = subparsers.add_parser("affine", help="Affine crypto system", parents=[parent])
affineparser.add_argument("-k", "--key", type=int, nargs=2, required=True, help="'a' and 'b' to be used in encryption")
affineparser.set_defaults(func=affine)

vigenereparser = subparsers.add_parser("vigenere", help="Vigenere crypto system", parents=[parent])
vigenereparser.add_argument("-k", "--key", type=str, required=True, help="Key string to be used in encryption")
vigenereparser.set_defaults(func=vigenere)

matrix = Matrix([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
hillparser = subparsers.add_parser("hill", help="Hill's crypto system", parents=[parent])
hillparser.add_argument("-k", "--key", type=str, default=matrix, help="Key matrix to be used in encryption")
hillparser.set_defaults(func=hill)

cracker = subparsers.add_parser("crack", help="Cracking encyphered text.")
cracker.add_argument("-c", "--cipher", type=str, help="Encyphered text to be decyphered by brute-force")
cracker.set_defaults(func=crack)

args = parser.parse_args()
