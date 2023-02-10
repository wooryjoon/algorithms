import sys
input = sys.stdin.readline
n = int(input())

d = [0] * 1000001
d[1] = 0
d[2] = 1
d[3] = 1
move = [0] * 1000001
move[1] = 0
move[2] = 1
move[3] = 1


for i in range(4,n+1):
    a = 999999
    b = 999999
    if i % 3 == 0 :
        a = d[i//3] + 1
        aa = i//3
    if i % 2 == 0 :
        b = d[i//2] + 1
        bb = i//2
    c = d[i-1] + 1
    cc = i-1
    d[i] = min(a,b,c)
    if d[i] == a:
        move[i] = aa
    elif d[i] == b :
        move[i] = bb
    elif d[i] == c :
        move[i] = cc

print(d[n])
ans = []
while n != 0 :
    ans.append(n)
    n = move[n]
print(' '.join(map(str,ans)))
