# e35.py

'''

The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from functions import pt, prime
from collections import deque

def rotations(m):
    dig = list(str(m))
    d = deque(dig)

    for i in range(len(dig)):
        d.rotate(1)
        yield int(''.join(d))


    #return (int(''.join(i)) for i in permutations(str(m)))

def circular(n):
    if all(pt(i) for i in rotations(n)):
        return True
    return False

if __name__ == '__main__':
    solutions = set()
    for i in prime(end=10**6):
        if circular(i):
            solutions.add(i)

    print(len(solutions))
