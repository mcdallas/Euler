# e37.py

'''
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from functions import pt, prime

def trunc(n):
    s = str(n)
    for i in range(1, len(s)):
        if not ( pt(int(s[i:])) and pt(int(s[:i])) ):
            return False

    return True

if __name__ == '__main__':
    solutions = set()

    for i in prime(n=11):
        if trunc(i):
            solutions.add(i)
        if len(solutions) >= 11:
            break

    print(sum(solutions))
