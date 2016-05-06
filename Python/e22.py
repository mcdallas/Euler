# e22.py

'''
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import requests
r = requests.get('https://projecteuler.net/project/resources/p022_names.txt')
s = r.text.split(',')
s = [ i[1:-1] for i in s]
s.sort()

def svalue(t):
    dic = {}
    for index, name in enumerate(t):
        sv = sum([ ord(i) - 64 for i in list(name)])
        dic[name] = sv * (index+1)
    return dic

if __name__ == '__main__':
    d = svalue(s)
    print(sum(d.values()))
