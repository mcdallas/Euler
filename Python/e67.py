# e67.py

'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''

import requests
from e18 import maxroute

r = requests.get('https://projecteuler.net/project/resources/p067_triangle.txt')
s = r.text.split('\n')
del s[-1]

n = [i.split(' ') for i in s]

k = []

for i in n:
    l = []
    for j in i:
        o = int(j)
        l.append(o)
    k.append(l)

print(maxroute(k)[0][0])
