# e4.py

'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def ispalindrome(n):
    l = list(str(n))
    if l == l[::-1]:
        return True
    return False

nums = set()

for i in range(100,1000):
    for j in range(100,1000):
        nums.add(i*j)

if __name__ == "__main__":
    print(max([n for n in nums if ispalindrome(n)]))
