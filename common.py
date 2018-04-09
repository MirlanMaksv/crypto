# Package of methods used commonly


# Euclidian algorithm: keep dividing while remainder is not thero.
# When remainder is thero previous remainder is GCD(a, b)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
