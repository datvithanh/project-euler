from common import sum_divisor

# nmax = 100
nmax = 28124
abundant = []

for i in range(2,nmax):
    if sum_divisor(i) > i: 
        abundant.append(i)

s = set()

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        if abundant[i] + abundant[j] >= nmax:
            break
        s.add(abundant[i] + abundant[j])

print(sum(list(range(nmax))) - sum(s))