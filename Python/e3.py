# e3.py

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

def prime_factors(n, fac=None):
    if not fac:
        fac = set()
    if n <= 3: return fac
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            fac.add(i)
            x = int(n/i)
            break

    else:
        fac.add(n)
        return fac

    return prime_factors(x, fac)

if __name__ == "__main__":
    print(max(prime_factors(600851475143)))
