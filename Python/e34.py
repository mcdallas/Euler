# e34.py

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial
from functions import digits

def curious(n):
    f = sum(factorial(i) for i in digits(n))
    if f == n:
        return True
    return False

if __name__ == '__main__':
    solutions = set()

    for i in range(10,10**6):
        if curious(i):
            solutions.add(i)

    print(sum(solutions))        
