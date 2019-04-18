from common import sum_divisor

sum_amicable_sumbers = 0

for i in range(2, 10000):
    sd = sum_divisor(i)
    if i%100 == 0:
        print(i)
    if sd != i and sum_divisor(sd) == i:
        sum_amicable_sumbers += i

print(sum_amicable_sumbers)
