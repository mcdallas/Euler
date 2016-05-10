from math import sqrt
from random import randint

def digits(n):
    #for i in list(str(n)):
    #    yield int(i)

    return [int(i) for i in list(str(n))]

# Primality test
def pt(n):
    if n < 2: return False
    for i in range(2,int(sqrt(n))+1):
        if not n % i:
            return False
    return True

def prime(n=2, end=float('inf')):
    while n <= end:
        if pt(n):
            yield n
        n += 1

def ispalindrome(n):
    l = list(str(n))
    if l == l[::-1]:
        return True
    return False

def mr(n, k=10):
    '''Miller–Rabin Primality Test'''
    assert n>3
    r, d = 0, n-1
    while d % 2 == 0:
        r += 1
        d = d//2

    for _ in range(k):
        flag = False
        a = randint(2, n-2)
        x = a**d % n
        if x == 1 or x == n-1:
            continue

        for _ in range(r-1):
            x = x**2 % n
            if x == 1:
                return False
            if x == n-1:
                flag = True
                break

        if flag:
            continue

        return False
    return True

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
