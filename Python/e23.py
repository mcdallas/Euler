from e21 import proper_factors

def abundants(n):
    abundant = set()

    for i in range(2, n+1):
        if sum(proper_factors(i)) > i:
            abundant.add(i)
    return abundant

if __name__ == '__main__':
    new = set()
    s = abundants(28123)
    for i in s:
        for j in s:
            new.add(i+j)

    print(sum(set(range(28124)) - new))
