import sys
input = sys.stdin.readline
from collections import deque
n,m = list(map(int,input().split()))# n개의배열, m번째를 계속 제거
arr = [i for i in range(1,n+1)]
#1 2 3 4 5 6 7

queue = deque(arr)

ans = []
count = 0

while(len(ans) != n) :
    x = queue.popleft()
    count += 1
    if count == m :
        count = 0
        ans.append(x)
        continue
    queue.append(x)
print('<' + ', '.join(map(str,ans)) + '>')



