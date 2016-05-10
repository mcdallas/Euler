# e39.py
# Runtime ~ 1:30
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

from math import sqrt
from collections import defaultdict

d = defaultdict(set)

for p in range(1,1001):
    for a in range(1,int(p/2)):
        for b in range(1,int((p-a)/2)):
            c = sqrt(a**2 + b**2)
            if c == p - a - b:
                d[p].add(frozenset((a,b,c)))

print(max(d, key=lambda x: len(d[x])))
