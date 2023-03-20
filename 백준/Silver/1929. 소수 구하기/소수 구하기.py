import sys
import copy
import math
input = sys.stdin.readline
from collections import deque
from heapq import heappush, heappop

# 에라토스테네스의 체

m,n = list(map(int,input().split()))

arr = [0] * (n+1)
ans = []
for i in range(2,n+1) :
    arr[i] = i

for i in range(2,int(math.sqrt(n))+1):
    if arr[i] == 0 : continue
    for j in range(i*2,n+1,i):
        if j % i == 0 : arr[j] = 0

for i in range(m,n+1):
    if arr[i] != 0 : ans.append(i)

print('\n'.join(map(str,ans)))