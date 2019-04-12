

multiple_factor_cnt = [0]*21

for i in range(2,21):
    factor_cnt = [0]*21
    x = i
    j = 2
    while(x!=1):
        if x%j == 0:
            x = x//j
            factor_cnt[j] += 1
        else:
            j = j+1
    for k in range(2,21):
        multiple_factor_cnt[k] = max(multiple_factor_cnt[k], factor_cnt[k])

smallest_multiple = 1

for i in range(2,21):
    smallest_multiple = smallest_multiple * i ** multiple_factor_cnt[i]

print(smallest_multiple)