from math import sqrt

def factors(n):
    fac = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            fac.add(i)
            fac.add(int(n/i))
    return fac

def triangle(n=1, end=float('inf')):
    while n <= end:
        yield sum(range(n+1))
        n += 1

for i, num in enumerate(triangle()):
    if len(factors(num)) >= 500:
        print(num)
        break
