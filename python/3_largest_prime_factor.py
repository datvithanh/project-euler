import math

n = 600851475143
# n = 3991
i = 2

while(i <= math.sqrt(n)):
    if n % i == 0:
        n = n//i
    else:
        i = i+1
        
print(n)
