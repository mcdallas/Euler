# e46.py

'''
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written
as the sum of a prime and twice a square?
'''

from functions import pt
from math import sqrt

def conjecture(n):
    x = int(sqrt(n/2))
    for i in range(1,x+1):
        if pt(n-2*(i**2)):
            return True
    return False

if __name__ == '__main__':
    i = 9
    while True:
        if not pt(i):
            if not conjecture(i):
                break
        i += 2

    print(i)
