"""


By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number
is the first example having seven primes among the ten generated numbers, yielding the family:

56003, 56113, 56333, 56443, 56663, 56773, and 56993.

Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.

"""

from itertools import permutations
from functions import prime
primes = set(prime(end=10**6))

def pt(n, primes=primes):
    return n in primes

def replace_digits(num, ndig):
    digs = tuple(str(num))
    for digits_to_replace in permutations(range(len(digs)), ndig):

            replaced = list(digs)
            family = []
            for digit in range(10):
                for digit_position in digits_to_replace:
                    replaced[digit_position] = str(digit)
                member = ''.join(replaced)
                if not member.startswith('0'):
                    family.append(int(member))
            yield family

n = 56003
continue_loop = True
while continue_loop and n < 10**6:
    length = len(str(n))
    for family in replace_digits(n, 3):
        if sum(pt(number) for number in family) == 8:
            print(family[0])
            continue_loop = False
            break
    n += 1
