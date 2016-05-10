# e47.py

'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
'''

from functions import prime_factors

i = 1
k = 0
while k < 4:
    i+= 1
    if len(prime_factors(i)) == 4:
        k += 1
    else:
        k=0

print(i-3)
