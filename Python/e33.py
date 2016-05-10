# e33.py

'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''
from fractions import Fraction

def frac(a,b):
    diga = [int(i) for i in list(str(a))]
    digb = [int(i) for i in list(str(b))]

    if a % 10 != 0 and b % 10 != 0:
        if diga[1] == digb[0]:
            if diga[0]/digb[1] == a/b:
                return True

    return False

if __name__ == '__main__':
    solutions = []
    for i in range(10,100):
        for j in range(i,100):
            if frac(i,j):
                solutions.append(Fraction(i,j))

    product = Fraction(1,1)
    for i in solutions:
        product *= i

    print(product.denominator)
