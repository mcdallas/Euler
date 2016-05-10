# e41.py

'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from functions import pt
from itertools import permutations

def pan(dig):
    for i in permutations('123456789'[:dig]):
        yield int(''.join(i))

if __name__ == '__main__':
    larger = 1
    for g in range(1,10):
        for i in pan(g):
            if pt(i) and i > larger:
                larger = i

    print(larger)
