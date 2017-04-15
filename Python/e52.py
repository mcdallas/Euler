"""

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""
from functions import digits

def generate_numbers(ndigits):
    start = 10**(ndigits-1)
    end = int(start * 10 / 6)
    yield from range(start, end+1)

def checkEqual(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)


def find_number(ndigits):
    for num in generate_numbers(ndigits):

        multiples = num, 2*num, 3*num, 4*num, 5*num, 6*num
        sorted_digits = [sorted(digits(m)) for m in multiples]
        if checkEqual(sorted_digits):
            print(num)
            return True
    return False

for ndigits in range(1, 10):
    if find_number(ndigits):
        break
