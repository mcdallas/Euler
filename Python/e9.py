d = set()
for a in range(1,1000):
    for b in range(1, 1000-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            d.add(frozenset([a, b, c]))

for triplet in d:
    p = 1
    for i in triplet:
        p *= i

print(p)
