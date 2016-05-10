# e45.py

'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

from e42 import is_triangular
from e44 import ispentagonal

def hexagonal(n=1, end=float('inf')):
    while n < end:
        yield 2*n**2 - n
        n += 1
        
for i in hexagonal(n=144):
    if ispentagonal(i) and is_triangular(i):
        break

print(i)
