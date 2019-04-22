
sum = 0
sum_sq = 0

for i in range(1,101):
    sum += i
    sum_sq += i**2

print(sum**2 - sum_sq)