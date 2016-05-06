# e6.py

'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sumsq(n):
    s = 0
    for i in range(1,n+1):
        s += i**2
    return s

def sqsum(n):
    s = sum(range(1,n+1))
    return s**2

if __name__ == "__main__":
    print(sqsum(100) - sumsq(100))
