# e31.py

'''
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

# Recursive solution, took me 4min to run

import numpy as np

solutions = set()
coins = (1, 2, 5, 10, 20, 50, 100, 200)

def change(n, cur=(0,0,0,0,0,0,0,0), p=0):
    global solutions
    global coins
    cur = list(cur)
    s = np.dot(cur,coins)

    if p >= 8:
        return 0

    for c in range(int((200 - s)/coins[p]) + 1):
        cur[p] = c
        if np.dot(cur, coins) == 200:
            solutions.add(tuple(cur))
        change(n, tuple(cur), p+1)

if __name__ == '__main__':
    change(200)
    print(len(solutions))
