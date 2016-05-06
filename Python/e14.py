def collatz(n):
    yield n
    while n != 1:

        if n % 2:
            n = 3*n+1
        else:
            n = int(n/2)
        yield n

d = {}

for i in range(1,1000001):
    d[i] = sum(1 for k in collatz(i))

print(max(d, key=lambda x:d[x]))            
