
f = open('data/p022_names.txt', 'r')

contents = f.read()

names = sorted([x[1:-1] for x in contents.split(',')])

result = 0
for key, name in enumerate(names):
    result += (key+1)*sum([ord(x)-ord('A') + 1 for x in name])
print(result)
