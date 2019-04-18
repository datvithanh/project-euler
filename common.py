from math import sqrt
import numpy as np


def isPrime(n):
    if n == 2:
        return True
    i = 1
    while i <= sqrt(n):
        i += 1
        if n % i == 0:
            return False
    return True


def count_divisors(x):
    factor_dict = {}
    j = 2
    while(x != 1):
        if x % j == 0:
            if j not in factor_dict.keys():
                factor_dict[j] = 1
            else:
                factor_dict[j] += 1
            x = x//j
        else:
            j = j+1

    return np.prod([x+1 for x in factor_dict.values()])

def sum_divisor(n):
    divisors = [1]
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            if i*i == n:
                divisors = divisors + [i]
            else:
                divisors = divisors + [i, n//i]
        i += 1

    return sum(divisors)
