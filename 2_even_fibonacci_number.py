
fib = [0]*40
fib[0] = 1
fib[1] = 2
i = 1

while(fib[i] <= 20):
    i += 1
    fib[i] = fib[i-1] + fib[i-2]

print(sum([x if x%2==0 else 0 for x in fib]))