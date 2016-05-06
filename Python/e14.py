# e14.py

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

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
