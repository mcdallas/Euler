# e32.py

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

def pandigit(a,b):
    l1 = list(str(a))
    l2 = list(str(b))
    l3 = list(str(a*b))

    s1 = set([int(i) for i in l1])
    s2 = set([int(i) for i in l2])
    s3 = set([int(i) for i in l3])

    if len(l1+l2+l3) == 9 and set(range(1,10)) == s1 | s2 | s3:
        return True
    return False

if __name__ == '__main__':
    solutions = set()
    for i in range(1, 10000):
        for j in range(1, int(10000/i)):
            if pandigit(i, j):
                solutions.add(i*j)

    print(sum(solutions))            
