import sys

input = sys.stdin.readline
# 반복문으로 넣고, while문으로 빼기
n = int(input())
arr = list(map(int,input().split()))
stack = []
ans = [0]* n
for i in range(n) :
    x = arr[i]
    if not stack : 
        stack.append((x,i)) # 값과 위치를 기록  
        continue
    while stack :
        if stack[-1][0] < x :
            ans[stack.pop()[1]] = x
        else :break
    stack.append((x,i))

for e in stack:
    ans[e[1]] = -1
print(' '.join(map(str,ans)))