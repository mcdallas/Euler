
def fib(end=float('inf')):
    n1, n2 = 1, 1
    yield n1
    yield n2
    n = 3
    while n <= end:
        yield n1 + n2
        n1, n2 = n2, n1 + n2
        n += 1

for i, num in enumerate(fib()):
    if num > 10**999:
        print(i+1)
        break
