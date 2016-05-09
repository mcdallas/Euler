# e36.py

'''

The decimal number, 585 = 10010010012 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
'''

from functions import ispalindrome

def dec_to_bin(x):
    return int(bin(x)[2:])

if __name__ == '__main__':
    solutions = set()
    for i in range(1,10**6):
        if ispalindrome(i) and ispalindrome(dec_to_bin(i)):
            solutions.add(i)

    print(sum(solutions))        
