from math import sqrt

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
