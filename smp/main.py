#! /usr/bin/python3
from parser import args
from sympy import Matrix

if __name__ == "__main__":
    kwargs = vars(args)
    if args.crypto == "hill":
        kwargs["key"] = Matrix(eval(args.key))

    et, dt = args.func(**kwargs)

    print("encrypted text -->", et)
    print("decrypted text -->", dt)
