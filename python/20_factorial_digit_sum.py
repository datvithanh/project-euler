res = 1

for i in range(1,101):
    res *= i

print(sum([int(tmp) for tmp in str(res)]))