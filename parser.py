from smp.crypto_sympy import caesar, affine, vigenere, autoclave, hill, rsa
from merkle_hellman import merkle_hellman 
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

autoclaveparser = subparsers.add_parser("autoclave", help="Autoclave crypto system", parents=[parent])
autoclaveparser.add_argument("-k", "--key", type=str, required=True, help="Key string to be used in encryption")
autoclaveparser.set_defaults(func=autoclave)

matrix = Matrix([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
hillparser = subparsers.add_parser("hill", help="Hill's crypto system", parents=[parent])
hillparser.add_argument("-k", "--key", type=str, default=matrix, help="Key matrix to be used in encryption")
hillparser.set_defaults(func=hill)

rsaparser = subparsers.add_parser("rsa", help="RSA crypto system", parents=[parent])
rsaparser.add_argument("--pqe", type=int, nargs=3, required=True, help="[p, q, e] to be used in encryption")
rsaparser.set_defaults(func=rsa)

mhparser = subparsers.add_parser("merkle-hellman", help="Merkle-Hellman crypto system", parents=[parent])
mhparser.add_argument("--S", type=int, nargs="*", required=True, help="Super increasing sequence")
mhparser.add_argument("--mod", type=int, required=True, help="m")
mhparser.add_argument("--a", type=int, required=True, help="a")
mhparser.set_defaults(func=merkle_hellman)

cracker = subparsers.add_parser("crack", help="Cracking encyphered text.")
cracker.add_argument("-c", "--cipher", type=str, required=True, help="Encyphered text to be decyphered by brute-force")
cracker.set_defaults(func=crack)

args = parser.parse_args()
