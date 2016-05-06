# e5.py

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from functools import reduce

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from math import gcd
    return reduce(gcd, numbers)


def lcm(*numbers):
    """Return lowest common multiple."""
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

if __name__ == "__main__":
    print(lcm(*list(range(1,21))))
