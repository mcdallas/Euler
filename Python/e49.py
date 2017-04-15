"""


The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""
from functions import pt

def digits(n):
    return list(str(n))

possible_starts = range(1000, 3341)

for x in possible_starts:
    x1, x2, x3 = x, x + 3330, x + 6660

    if x1 == 1487:
        continue

    if sorted(digits(x1)) == sorted(digits(x2)) == sorted(digits(x3)) and all((pt(x1), pt(x2), pt(x3))):
        print(int(''.join(digits(x1) + digits(x2) + digits(x3))))
