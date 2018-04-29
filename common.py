# Package of methods used commonly


# Euclidian algorithm: keep dividing while remainder is not thero.
# When remainder is thero previous remainder is GCD(a, b)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Checks if a and b are relatively prime numbers
def arelprimes(a, b):
    return gcd(a, b) == 1


# Generates relatively prime number of a
def relprimes(a):
    rprimes = []
    for i in range(a):
        if arelprimes(i, a):
            rprimes.append(i)
    return rprimes
