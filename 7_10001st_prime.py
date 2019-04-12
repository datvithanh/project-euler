from common import isPrime

cnt = 0
i = 1

while cnt < 10001:
    i += 1
    if isPrime(i):
        cnt += 1

print(i)