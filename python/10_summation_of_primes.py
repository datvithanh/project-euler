from common import isPrime

s = 0

for i in range(2, 2000000):
    if isPrime(i):
        s += i

print(s)