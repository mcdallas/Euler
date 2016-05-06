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
