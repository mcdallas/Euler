from itertools import permutations, islice

l = next(islice(permutations(range(10)), 999999, 1000000))
l = [str(i) for i in l]

print(''.join(l))
