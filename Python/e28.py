# e28.py

'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

import numpy as np

# Create an empty 1001x1001 array
N = np.zeros((1001,1001))

N[500,500] = 1

def right(mat, i, j, num):
    mat[i, j+1] = num + 1
    return mat, i, j+1,  num + 1

def down(mat, i, j, num):
    mat[i+1, j] = num + 1
    return mat, i+1, j,  num + 1

def left(mat, i, j, num):
    mat[i, j-1] = num + 1
    return mat, i, j-1,  num + 1

def up(mat, i, j, num):
    mat[i-1, j] = num + 1
    return mat, i-1, j,  num + 1

coords = (N, 500, 500, 1)

# fill the array
for i in range(1,1001):
    if i % 2 == 1:
        for k in range(i):
            coords = right(*coords)
        for k in range(i):
            coords = down(*coords)

    else:
        for k in range(i):
            coords = left(*coords)
        for k in range(i):
            coords = up(*coords)

for k in range(1000):
    coords = right(*coords)

print(int(N.trace() + N[::-1].trace())-1)
