import requests
from e18 import maxroute

r = requests.get('https://projecteuler.net/project/resources/p067_triangle.txt')
s = r.text.split('\n')
del s[-1]

n = [i.split(' ') for i in s]

k = []

for i in n:
    l = []
    for j in i:
        o = int(j)
        l.append(o)
    k.append(l)

print(maxroute(k)[0][0])    
