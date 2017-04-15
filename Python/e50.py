"""


The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""

from functions import prime, pt

# list_of_primes = list(prime(end=10**6))
# set_of_primes = set(list_of_primes)
primes = list(prime(end=10**6))

max_consec = (21, 0, 0)

for ind, p in enumerate(primes):
    for i in range(max_consec[0], len(primes) - ind):

        tempsum = sum(primes[ind:ind + i])
        if tempsum >= 10**6:
            break
        if pt(tempsum):
            max_consec = (i, p, tempsum)


print(max_consec[2])
