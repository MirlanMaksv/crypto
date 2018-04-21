from crypto_sympy import caesar, affine
import argparse

descr = "Encryption and decryption using sympy package"
parser = argparse.ArgumentParser(description=descr)
subparsers = parser.add_subparsers()

caesarparser = subparsers.add_parser("caesar", help="Caesar crypto system")
caesarparser.add_argument("-m", "--msg", type=str, required=True, help="Message to be encrypted then decrypted")
caesarparser.add_argument("-k", "--key", type=int, required=True, help="Key to be used in encryption")
caesarparser.set_defaults(func=caesar)

affineparser = subparsers.add_parser("affine", help="Affine crypto system")
affineparser.add_argument("-m", "--msg", type=str, required=True, help="Message to be encrypted then decrypted")
affineparser.add_argument("--ab", type=int, nargs=2, required=True, help="'a' and 'b' to be used in encryption")
affineparser.set_defaults(func=affine)

args = parser.parse_args()
