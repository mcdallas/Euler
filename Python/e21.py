from e12 import factors

def proper_factors(n):
    f = factors(n)
    f.remove(n)
    return f

def amicable(n):
    amicables = set()
    for i in range(2, n+1):
        s = sum(proper_factors(i))
        if sum(proper_factors(s)) == i and i != s:
            amicables.update((i,s))
    return amicables

if __name__ == '__main__':
    print(sum(amicable(10000)))
