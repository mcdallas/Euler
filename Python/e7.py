# e7.py

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from itertools import islice
from math import sqrt

# Primality test
def pt(n):
     for i in range(2,int(sqrt(n))+1):
         if not n % i:
             return False
     return True

def prime(n=2, end=float('inf')):
    while n <= end:
        if pt(n):
            yield n
        n += 1

def nth(n, gen):
    return next(islice(gen(),n-1 ,n))

if __name__ == "__main__":
    print(nth(10001, prime))
