
for a in range(0, 1000):
    for b in range(a, 1000):
        if a + b < 1000:
            x = min([a, b, 1000-a-b])
            z = max([a, b, 1000-a-b])
            y = 1000 - x - z
            if x**2 + y ** 2 == z**2:
                print(x*y*z)
                print(x,y,z)
