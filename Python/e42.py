# e42.py

'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value. For example, the word
value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number
then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
'''

import requests
from math import sqrt

def is_triangular(n):
    n = 2 * n
    s = int(sqrt(n))
    if n == s * (s + 1):
        return True
    return False

r = requests.get('https://projecteuler.net/project/resources/p042_words.txt')
s = r.text.split(',')
s = [ i[1:-1] for i in s]

def value(word):
    return sum([ord(i) - 64 for i in list(word)])

if __name__ == '__main__':
    print(sum(1 for w in s if is_triangular(value(w))))    
