
def isPalindrome(n):
    n = str(n)
    for i in range(int(len(n)/2)+1):
        if n[i] != n[-i-1]:
            return False
    return True

max_palindrome = 0

for i in reversed(range(100,1000)):
    for j in reversed(range(100,1000)):
        if isPalindrome(i*j):
            max_palindrome = max(max_palindrome, i*j)

print(max_palindrome)
