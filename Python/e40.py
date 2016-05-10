# e40.py

'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

from itertools import islice

def dec(end=float('inf')):
    n = 1
    while n <= end:
        for i in str(n):
            yield int(i)
        n += 1

def d(n):
    return next(islice(dec(), n-1, n))

if __name__ == '__main__':
    print(d(1) * d(10) * d(100)  * d(1000) * d(10000) * d(100000) * d(1000000))
