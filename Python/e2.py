fibon = {1: 1, 2: 1}

def fib(n):
    global fibon
    if n in fibon:
        return fibon[n]
    else:
        res = fib(n-1) + fib(n-2)
        fibon[n] = res
        return res

def evens(limit):
    k = 1
    l = 1
    while k <= limit:
        if not k % 2:
            yield k
        l += 1
        k = fib(l)

if __name__ == "__main__":
    print(sum(evens(4000000)))        
