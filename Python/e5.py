from functools import reduce

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from math import gcd
    return reduce(gcd, numbers)


def lcm(*numbers):
    """Return lowest common multiple."""
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

if __name__ == "__main__":
    print(lcm(*list(range(1,21))))
