from math import sqrt

def isPrime(n):
    if n == 2:
        return True
    i = 1
    while i <= sqrt(n):
        i += 1
        if n % i == 0:
            return False
    return True