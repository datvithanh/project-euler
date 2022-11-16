#bignum

x = [0] * 10
mark = [0] * 10
count = 0

def permutations(n):
    global count
    if n == 10:
        count += 1
        if count == 1000000:
            print(x)
            exit(0)
    else:
        for i in range(10):
            if mark[i] == 0:
                mark[i] = 1
                x[n] = i
                permutations(n + 1)
                mark[i] = 0
    
    
permutations(0)