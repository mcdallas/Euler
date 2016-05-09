# e38.py

'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital,
192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

from functions import digits

def pandigital(n):
    if len(str(n)) == 9 and set(digits(n)) == set(range(1,10)):
        return True
    return False

def concat(it):
    s = [str(i) for i in it]
    return int(''.join(s))

def prod(n, m):
    return (n*i for i in range(1,m+1))

if __name__ == '__main__':
    solutions = set()

    for n in range(1,10000):
        for m in range(2,10):
            c = concat(prod(n,m))
            if pandigital(c):
                solutions.add(c)

    print(max(solutions))
