"""

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""

def pow_mod_10(n):
    return n**n % 10**10

tempsum = 0

for x in range(1, 1001):
    tempsum = (tempsum + pow_mod_10(x)) % 10**10

print(tempsum)
