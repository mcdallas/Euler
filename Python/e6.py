def sumsq(n):
    s = 0
    for i in range(1,n+1):
        s += i**2
    return s

def sqsum(n):
    s = sum(range(1,n+1))
    return s**2

if __name__ == "__main__":
    print(sqsum(100) - sumsq(100))    
