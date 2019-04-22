
def collatz_seq_len(n):
    seq = []
    while n not in seq:
        seq.append(n)
        n = n//2 if n%2 == 0 else 3*n + 1
    return len(seq)

maxlen = 0

for i in range(1000000):
    if i % 1e4 == 0:
        print(i)
    maxlen = max(maxlen, collatz_seq_len(i))
    
print(maxlen)    