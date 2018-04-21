import argparse

descr = "Encryption and decryption using sympy package"
parser = argparse.ArgumentParser(description=descr)
parser.add_argument("--crypto", type=str, required=True, help="Cryptography method to be appllied")
parser.add_argument("--msg", type=str, required=True, help="Message to be encrypted then decrypted")
parser.add_argument("--key", type=int, required=False, help="Key to be used in encryption")
args = parser.parse_args()
