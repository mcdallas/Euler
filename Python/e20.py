from math import factorial

def sum_digits(n):
    l = list(str(n))
    return sum([int(i) for i in l])

print(sum_digits(factorial(100)))    
