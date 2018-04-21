#! /usr/bin/python3
from parser import args

if __name__ == "__main__":
    et, dt = args.func(**vars(args))
    
    print("encrypted text -->", et)
    print("decrypted text -->", dt)
