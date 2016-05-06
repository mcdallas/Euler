# e27.py

'''
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
'''

from e7 import pt, prime

def quad_primes(a,b):
    n = 0
    while n**2 + a*n + b > 0 and pt(n**2 + a*n + b):
        n += 1

    return n

if __name__ == '__main__':
    d = {}
    for a in range(-1000, 1001):
        # only iterate over primes since n(0) = b must be a prime
        for b in prime(end=1000):
            d[(a,b)] = quad_primes(a,b)

    coef = max(d, key=lambda x: d[x])
    print(coef[0]*coef[1])
