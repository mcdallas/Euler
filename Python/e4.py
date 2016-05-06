def ispalindrome(n):
    l = list(str(n))
    if l == l[::-1]:
        return True
    return False

nums = set()

for i in range(100,1000):
    for j in range(100,1000):
        nums.add(i*j)

if __name__ == "__main__":
    print(max([n for n in nums if ispalindrome(n)]))        
