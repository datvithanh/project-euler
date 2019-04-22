from common import count_divisors


i = 7
n = 28
while True:
    i += 1
    n += i
    if count_divisors(n) > 500:
        print(n)
        break