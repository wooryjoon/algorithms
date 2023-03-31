import sys
def gcd(a, b):
    if(a == 0):
        return b
    return gcd(b % a, a)
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
g = gcd(s[0], gcd(s[1], s[-1]))
for i in range(1, (g // 2) + 1):
    if g % i == 0:
        print(i)
print(g)